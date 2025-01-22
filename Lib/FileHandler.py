# Lib/FileHandler.py

import os
import shutil
import logging
from datetime import datetime
from configparser import ConfigParser
import re

class FileHandler:
    def __init__(self, config_path='Config/config.ini'):
        # Load configuration
        self.config = ConfigParser()
        self.config.read(config_path)
        self.setup_logging()
    
    def setup_logging(self):
        # Set up logging configuration
        log_dir = self.config.get('Directories', 'log_dir')
        os.makedirs(log_dir, exist_ok=True)
        
        log_file = os.path.join(
            log_dir, 
            f'process_log_{datetime.now().strftime("%Y%m%d")}.log'
        )
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )

    def validate_file_pattern(self, filename):
        # Check if file matches pattern and is not already archived
        pattern = r'^[a-zA-Z0-9_]+_logs_\d{8}\.logs$'
        prefix = self.config.get('FilePatterns', 'archive_prefix')
        
        # Skip files that already start with archive_
        if filename.startswith(f"{prefix}_"):
            return False
            
        return bool(re.match(pattern, filename))

    def get_source_files(self):
        # Get all valid log files
        source_dir = self.config.get('Directories', 'source_dir')
        files = []
        
        try:
            for file in os.listdir(source_dir):
                if self.validate_file_pattern(file):
                    full_path = os.path.join(source_dir, file)
                    files.append(full_path)
                    logging.info(f"Found valid file: {file}")
                else:
                    logging.debug(f"Skipping invalid or already processed file: {file}")
            
            logging.info(f"Found {len(files)} files to process")
            return files
            
        except Exception as e:
            logging.error(f"Error accessing source directory: {e}")
            raise

    def generate_new_filename(self, original_file):
        # Create new filename with archive prefix
        prefix = self.config.get('FilePatterns', 'archive_prefix')
        filename = os.path.basename(original_file)
        return f"{prefix}_{filename}"

    def move_and_rename_file(self, source_file):
        # Move and rename a single file
        try:
            audit_dir = self.config.get('Directories', 'audit_dir')
            new_filename = self.generate_new_filename(source_file)
            target_path = os.path.join(audit_dir, new_filename)
            
            os.makedirs(audit_dir, exist_ok=True)
            
            if os.path.exists(target_path):
                logging.warning(f"Target file already exists: {target_path}")
                return False
                
            shutil.move(source_file, target_path)
            logging.info(f"Successfully moved: {source_file} -> {target_path}")
            return True
            
        except Exception as e:
            logging.error(f"Error processing file {source_file}: {e}")
            return False

    def process_files(self):
        try:
            files = self.get_source_files()
            
            if not files:
                logging.info("No new files to process")
                return 0
                
            processed_count = 0
            for file in files:
                if self.move_and_rename_file(file):
                    processed_count += 1
                    
            logging.info(f"Processing complete. {processed_count}/{len(files)} files processed successfully")
            return processed_count
            
        except Exception as e:
            logging.error(f"Error during file processing: {e}")
            raise
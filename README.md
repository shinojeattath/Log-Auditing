Log Archival System
A Python-based automation tool for managing application log files. This system automatically renames and moves log files from a source directory to an audit directory following specified naming conventions.
Features

Automated log file processing
Cross-platform compatibility (Windows & Linux)
Standardized file naming convention
Detailed operation logging
Error handling and reporting
Configurable directory paths
Modular and reusable design

Prerequisites

Python 3.6 or higher
Required Python packages:

configparser
logging
os
shutil
re
datetime



Project Structure
CopyProject/
├── Config/
│   └── config.ini           # Configuration settings
├── Lib/
│   └── FileHandler.py       # Core file handling logic
├── Logs/
│   └── process_log_<YYYYMMDD>.log  # Execution logs
├── Main.py                  # Main execution script
├── Source/                  # Original log files
├── Audit/                   # Processed log files
└── README.md
Installation

Clone or download the project repository
Create the required directories:

bashCopymkdir -p Project/Config Project/Lib Project/Logs Project/Source Project/Audit

Copy the provided files to their respective directories:

config.ini → Config/
FileHandler.py → Lib/
Main.py → Project root



Configuration
Edit Config/config.ini to customize:
iniCopy[Directories]
source_dir = Source
audit_dir = Audit
log_dir = Logs

[FilePatterns]
log_file_pattern = *_logs_*.logs
archive_prefix = archive
Usage

Place log files in the Source directory following the naming convention:

Format: <application_name>_logs_<YYYYMMDD>.logs
Example: app1_logs_20250120.logs


Run the script:

bashCopypython Main.py

Check results:

Processed files will be in the Audit directory
Operation logs will be in the Logs directory



File Naming Convention

Original files: <application_name>_logs_<YYYYMMDD>.logs
Processed files: archive_<application_name>_logs_<YYYYMMDD>.logs

Logging

Log files are created daily
Location: Logs/process_log_YYYYMMDD.log
Contains:

File movement operations
Errors and exceptions
Processing statistics



Error Handling
The system handles various scenarios:

Invalid file names
Missing directories (auto-creates them)
File access permissions
Duplicate files
Processing failures

Troubleshooting
Common issues and solutions:

Permission Denied

Ensure proper file and directory permissions
Run with appropriate user privileges


Files Not Processing

Check file naming convention
Verify source directory path
Check log files for specific errors


Script Fails to Start

Verify Python installation
Check all required directories exist
Ensure config.ini is properly formatted
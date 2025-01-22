from Lib.FileHandler import FileHandler
import logging
import sys

def main():
    try:
        handler = FileHandler()
        processed_count = handler.process_files()
        sys.exit(0 if processed_count > 0 else 1)
    except Exception as e:
        logging.error(f"Critical error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
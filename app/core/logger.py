import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Log file path
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "yatra_saathi.log"

# Create formatter
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# File handler (rotates every 1MB, keeps 5 backups)
file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=5)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# Root logger configuration
logging.basicConfig(
    level=logging.INFO,
    handlers=[console_handler, file_handler]
)

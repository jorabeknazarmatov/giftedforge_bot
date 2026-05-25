import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s %(filename)s:%(lineno)d - %(message)s")

logger = logging.getLogger("bot")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler(log_dir / "bot.log")
file_handler.setLevel(logging.DEBUG)



file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

file_handler = RotatingFileHandler(filename=log_dir / "bot.log", maxBytes=5 * 1024 * 1024, backupCount=3, encoding='utf-8')


logger.addHandler(file_handler)
logger.addHandler(console_handler)
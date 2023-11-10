import logging
import os
from datetime import datetime


class Logger:
    """Logger for Test Automation Framework."""

    DEFAULT_LEVEL = logging.DEBUG
    DEFAULT_FORMATTER = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S"
    )

    def __init__(self):
        self.logs_dir_path = self._create_logs_directory()
        self.log_file_path = self._create_log_file_path()

    def _create_logs_directory(self):
        """
        Internal function which returns the path to logs directory
        and create logs directory if it doesn't exist.
        """

        dir_path = os.path.abspath(__file__)

        for i in range(3):
            dir_path = os.path.dirname(dir_path)

        logs_dir_path = os.path.join(dir_path, "tests", "logs")

        if not os.path.exists(logs_dir_path):
            os.makedirs(logs_dir_path)

        return logs_dir_path

    def _create_log_file_path(self):
        """
        Internal function which returns the path to log file
        and create logs directory for specific day if it doesn't exist.
        """

        log_dir_path = os.path.join(
            self.logs_dir_path, f"logs_{datetime.now().strftime('%d%m%y')}"
        )

        if not os.path.exists(log_dir_path):
            os.makedirs(log_dir_path)

        log_file_path = os.path.join(
            log_dir_path,
            f"testlog_{datetime.now().strftime('%d%m%y_%H%M%S')}.log"
        )

        return log_file_path

    def get_file_handler(self, formatter):
        """
        Function which returns file handler, set formatter for it
        and prepares log file to which logs will be sent.
        """

        file_handler = logging.FileHandler(filename=self.log_file_path, mode="a")
        file_handler.setFormatter(formatter)

        return file_handler

    def get_logger(self, logger_name, level=DEFAULT_LEVEL, formatter=DEFAULT_FORMATTER):
        """
        Function which returns logger, set logging level for it
        and add handler(s). Handlers send the log records created by loggers
        to the appropriate destination.
        """

        logger = logging.getLogger(logger_name)
        logger.setLevel(level)
        logger.addHandler(self.get_file_handler(formatter))

        return logger


AFLogger = Logger()


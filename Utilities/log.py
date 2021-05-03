import inspect
import logging
import sys


def custom_logger(log_level=logging.DEBUG, filename='log.log', logger_name=""):
    # Set logger_name to class or method name
    if logger_name == "": logger_name = inspect.stack()[1][3]

    # Create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # Create handler
    file_handler = logging.FileHandler \
        (filename=filename, mode="a")
    file_handler.setLevel(log_level)

    # Create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                                  datefmt="%d/%m/%Y %I:%M:%S %p")

    # Pass formatter to handler
    file_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(file_handler)

    # # console logs
    # stdout_handler = logging.StreamHandler(sys.stdout)
    # stdout_handler.setLevel(log_level)
    # stdout_handler.setFormatter(formatter)
    # logger.addHandler(stdout_handler)
    #
    return logger

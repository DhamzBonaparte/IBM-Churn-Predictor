import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="log.log",
#     filemode="w",
#     format="%(asctime)s - %(levelname)s - %(message)s",
# )

logger = logging.getLogger(__name__)
handler = logging.FileHandler("test.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

x = 2
logger.debug("The value of x is %d", x)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Cant divide by zero")

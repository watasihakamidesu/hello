import logging

logging.basicConfig(level=logging.DEBUG,
              #  format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                format='[%(asctime)s] %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='cloud.log',
                filemode='a')

logging.warning("This is warning message")
logging.debug("This is debug message")
logging.info("This is info message")

import logging
import inspect

class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("D:\\programming\\OrangeHrm\\Log\\OrgHrm.log")
        log_format = logging.Formatter("%(asctime)s : %(filename)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(log_format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger

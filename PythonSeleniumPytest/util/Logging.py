import logging
import inspect

#class LogConsole:
def LogConsole():
    testname = inspect.stack()[1][3]
    logger = logging.getLogger(testname)
    logger.setLevel(logging.DEBUG)
    loghandler = logging.FileHandler(filename="PythonSeleniumPytest/autotest.log", mode='w')
    #filename = "PythonSeleniumPytest/"+__class__+".log"
    #loghandler = logging.FileHandler(filename="PythonSeleniumPytest/autotest.log", mode='w')
    loghandler.setLevel(logging.DEBUG)
    logformat = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
    loghandler.setFormatter(logformat)
    logger.addHandler(loghandler)
    return logger



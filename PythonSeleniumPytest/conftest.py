import pytest
from PythonSeleniumPytest.base.SeleniumWebDriver import SeleniumWebDriverInit
from PythonSeleniumPytest.util.Logging import LogConsole

@pytest.fixture(scope="class")
def SetupAndTeardown(request, browser):
    di = SeleniumWebDriverInit()
    driver = di.DriverSetup(browser)
    log = LogConsole()
    log.info("Startup")
    if request.cls is not None:
        request.cls.driver = driver
        request.cls.log = log
    yield driver, log
    driver.quit()
    log.info("Teardown")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")





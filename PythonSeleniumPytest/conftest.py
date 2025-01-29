import pytest
from PythonSeleniumPytest.base.SeleniumWebDriver import SeleniumWebDriverInit
from PythonSeleniumPytest.util.Logging import LogConsole

@pytest.fixture(scope="session")
def SetupAndTeardown(request,browser):
    di = SeleniumWebDriverInit()
    driver = di.DriverSetup(browser)
    log = LogConsole()
    log.info("Startup")
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
        setattr(cls.obj, "log", log)
    yield
    driver.quit()
    log.info("Teardown")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")





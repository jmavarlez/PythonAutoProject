class FrameWindowHandler:

    def __init__(self, driver):
        self.driver = driver


    def iframeaccess(self, iframename):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, iframename))


    def mainframeaccess(self):
        self.driver.switch_to.default_content()
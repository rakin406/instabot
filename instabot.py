from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


class Instabot:
    """
    Instagram chatbot
    """

    def __init__(self):
        # Run headless profiled browser
        self.__options = Options()
        self.__options.headless = True
        self.__driver = webdriver.Firefox(
            webdriver.FirefoxProfile(self.__get_profile_path()), options=self.__options
        )
        self.__driver.get("https://www.instagram.com/direct/inbox/")

    def __rchop(self, s: str, suffix: str) -> str:
        """
        Remove last occurence of the substring.
        """
        if suffix and s.endswith(suffix):
            return s[: -len(suffix)]
        return s

    def __get_profile_path(self) -> str:
        """
        Get current Firefox profile path.
        """
        # Run headless browser
        options = Options()
        options.headless = True
        unprofiled_driver = webdriver.Firefox(options=options)

        unprofiled_driver.get("about:profiles")
        profile = unprofiled_driver.find_elements_by_tag_name("td")[1].text
        profile = self.__rchop(profile, "Open Directory")
        unprofiled_driver.quit()
        return profile

    def find_person(self, username: str):
        """
        Find and click the person.
        """
        try:
            person = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), '{}')]".format(username))
                )
            )
        except Exception:
            # Too slow internet connection
            pass
        person.click()

    def text_person(self, text: str):
        """
        Text the person on instagram.
        """
        input_area = self.__driver.find_element_by_tag_name("textarea")
        input_area.send_keys(text)
        input_area.send_keys(Keys.RETURN)

    def get_message(self) -> str:
        """
        Get the person's last message.
        """
        try:
            message = self.__driver.find_elements_by_tag_name("span")[-1].text
            return message
        except Exception:
            pass
        return None

    def stop(self):
        """
        Terminate the bot.
        """
        self.__driver.quit()

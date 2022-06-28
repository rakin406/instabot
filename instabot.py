from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


class Instabot:
    """
    Instagram chatbot
    """

    def __init__(self):
        # Run headless profiled browser
        self.__options = Options()
        self.__options.headless = False
        self.__driver = webdriver.Firefox(
            webdriver.FirefoxProfile(self.__get_profile_path()), options=self.__options
        )


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

    def open_chat(self, username: str):
        """
        Find person and open the chat.
        """
        self.__driver.get("https://www.instagram.com/{}/".format(username))
        sleep(2)
        chat = self.__driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div")
        chat.click()
        sleep(4)

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
        return ""

    def stop(self):
        """
        Terminate the bot.
        """
        self.__driver.quit()

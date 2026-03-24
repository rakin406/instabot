import os
import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class InstaChat:
    """
    Instagram chat automation
    """

    def __init__(self):
        user_data_dir = self.__get_user_data_dir()

        # Set Chromium options
        options = Options()
        options.add_argument(f"--user-data-dir={user_data_dir}")
        options.add_argument(f"--profile-directory=Default")
        # options.add_argument("--headless=new")  # Run headless
        options.add_argument(
            "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
        )  # Set user agent
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--enable-automation")
        options.add_argument(
            "--disable-blink-features=AutomationControlled"
        )  # Reduces detection

        self.__driver = webdriver.Chrome(options=options)
        self.__driver.implicitly_wait(10)

    def open_chat(self, username: str):
        """
        Find person and open the chat.
        """
        url = "https://www.instagram.com/" + username
        self.__driver.get(url)
        chat = self.__driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div"
        )
        chat.click()

    def text_person(self, text: str):
        """
        Text the person on instagram.
        """
        input_area = self.__driver.find_element_by_tag_name("textarea")
        input_area.send_keys(text + Keys.ENTER)

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
        Terminate InstaChat.
        """
        self.__driver.quit()

    def __get_user_data_dir(self) -> str | None:
        os_name = platform.system()
        user_data_dir = None

        # Find user data path
        if os_name == "Windows":
            user_data_dir = os.path.expandvars(r"%LOCALAPPDATA%\Chromium\User Data")
        elif os_name == "Linux":
            user_data_dir = os.path.expanduser("~/.config/chromium")
        elif os_name == "Darwin":
            user_data_dir = os.path.expanduser("~/Library/Application Support/Chromium")

        return user_data_dir

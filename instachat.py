import sys
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class InstaChat:
    """
    Instagram chat automation
    """

    def __init__(self):
        # TODO: Bulletproof login.
        self.USER_DATA_DIR = ".user-data"

        has_user_data = Path(self.USER_DATA_DIR).is_dir()

        # Create user data directory
        Path(self.USER_DATA_DIR).mkdir(parents=True, exist_ok=True)

        # Set Chromium options
        options = Options()
        options.add_argument(f"--user-data-dir={self.USER_DATA_DIR}")
        options.add_argument("--headless=new")  # Run headless
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument(
            "--disable-blink-features=AutomationControlled"
        )  # Reduces detection
        options.add_argument("--password-store=basic")

        self.__driver = webdriver.Chrome(options=options)

        # NOTE: This is a bad technique even though it works.
        # Login
        if not has_user_data:
            print("Please login to Instagram within 2 minutes and restart the program.")
            self.__driver.get("https://www.instagram.com")
            time.sleep(120)
            sys.exit(0)

        self.__driver.implicitly_wait(10)

    def __del__(self):
        """
        Cleanup function.
        """
        self.__driver.quit()

    def open_chat(self, username: str):
        """
        Find person and open the chat.
        """
        url = "https://www.instagram.com/" + username
        self.__driver.get(url)
        chat = self.__driver.find_element(
            By.XPATH, "//div[contains(text(), 'Message')]"
        )
        chat.click()

    def get_last_message(self) -> str | None:
        """
        Get the person's last message.
        """
        messages = self.__driver.find_elements(
            By.CSS_SELECTOR, "div.html-div[dir='auto']"
        )
        return messages[-1].text if messages else None

    def send_message(self, message: str):
        """
        Send message in the opened chat window on Instagram.
        """
        textarea = self.__driver.find_element(By.CSS_SELECTOR, "p[dir='auto']")
        textarea.clear()
        textarea.send_keys(message + Keys.ENTER)

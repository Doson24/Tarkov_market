from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def init_webdriver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Режим без интерфейса
    # chrome_options.add_argument('--start-fullscreen')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument('--disable-dev-shm-usage')

    # chrome_options.add_argument("--start-maximized")
    #в режиме headless без user-agent не загружает страницу
    chrome_options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"'')
    # self.driver = webdriver.Chrome('C:\\install\\chromedriver.exe', options=chrome_options)
    driver = webdriver.Chrome('C:\\install\\chromedriver.exe', options=chrome_options)
    return driver
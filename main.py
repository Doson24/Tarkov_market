import datetime
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from init_driver_selenium import init_webdriver
from selenium.webdriver.support.wait import WebDriverWait

import pandas as pd


def scroll(driver):
    try:
        driver.find_element(By.CLASS_NAME, 'big.bold.w-100.text-center.py-10').send_keys(Keys.ENTER)
    except Exception as ex:
        print(ex)
    rows = driver.find_element(By.CLASS_NAME, 'table-list').find_elements(By.CLASS_NAME, 'row')
    count_rows = len(rows)

    ActionChains(driver) \
        .scroll_to_element(rows[-1])\
        .perform()

    time.sleep(1)
    while count_rows < len(driver.find_element(By.CLASS_NAME, 'table-list').find_elements(By.CLASS_NAME, 'row')):
        rows = driver.find_element(By.CLASS_NAME, 'table-list').find_elements(By.CLASS_NAME, 'row')
        time.sleep(2)
        ActionChains(driver) \
            .scroll_to_element(rows[-1]) \
            .send_keys(Keys.PAGE_DOWN)\
            .perform()
        # WebDriverWait(driver, timeout=10).until(document_initialised)
        count_rows = len(rows)


def parse_page(driver):
    names, changes_24h, changes_7d, avg_prices24h, prices_sell_trader, names_trader = [], [], [], [], [], []
    rows = driver.find_element(By.CLASS_NAME, 'table-list').find_elements(By.CLASS_NAME, 'row')
    # row[0] это заголовки таблицы
    for row in rows[1:]:
        div = row.find_element(By.CLASS_NAME, 'full-width')

        name = div.find_element(By.TAG_NAME, 'a').text
        change_24h = row.find_elements(By.CLASS_NAME, 'cell')[4].text
        change_7d = row.find_elements(By.CLASS_NAME, 'cell')[5].text
        avg_price_24h = row.find_element(By.CLASS_NAME, 'price-main').text

        sell_to_trader = row.find_elements(By.CLASS_NAME, 'cell')[6].text
        price_sell_trader, name_trader = sell_to_trader.split('\n')

        names.append(name)
        changes_24h.append(change_24h)
        changes_7d.append(change_7d)
        avg_prices24h.append(avg_price_24h)
        prices_sell_trader.append(price_sell_trader)
        names_trader.append(name_trader)

    return pd.DataFrame({
        'Date': datetime.date.today().strftime('%d-%m-%Y'),
        'Name': names,
        'avg_price_24h': avg_prices24h,
        'change_24h': changes_24h,
        'change_7d': changes_7d,
        'price_sell_trader': prices_sell_trader,
        'name_trader': names_trader
    })


def main(driver):
    base_url = 'https://tarkov-market.com/ru/tag/'
    categories = ['keys', 'barter', 'containers', 'provisions', 'gear', 'meds',
                  'sights', 'suppressors', 'weapon', 'ammo', 'magazines', 'tactical_devices',
                  'weapon_parts', 'special_equipment', 'maps', 'ammo_boxes', 'repair']
    driver.set_window_size(1920, 1080)
    data = pd.DataFrame()
    for category in categories:
        driver.get(base_url + category)
        scroll(driver)
        df = parse_page(driver)
        df['category'] = category
        data = pd.concat([data, df], ignore_index=True)
        print(f'------- download {category} {len(df)} items done -------')
        time.sleep(1)
    data.to_csv(f'data\data{datetime.date.today().strftime("%d-%m-%Y")}.csv')
    print(f'count items -  {len(data)}')


if __name__ == '__main__':
    driver = init_webdriver()
    start_time = time.time()
    main(driver)
    driver.quit()
    print("--- %s seconds ---" % (time.time() - start_time))
    time.sleep(30)

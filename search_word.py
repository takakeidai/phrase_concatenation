import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def set_driver(driver_path, headless_flg):

    if "chrome" in driver_path:
          options = ChromeOptions()
    else:
      options = Options()

    if headless_flg == True:
        options.add_argument('--headless')

    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')        

    driver_path = ChromeDriverManager().install()
    return Chrome(executable_path=driver_path, options=options)


def search_word(sub_word):
    word_list = []
    driver_path = ChromeDriverManager().install()
    
    # Chromeを立ち上げたくないならTrueを入れればいい。
    driver = set_driver(driver_path, False)
    driver.get("https://www.weblio.jp/")
    time.sleep(1)
    
    #コンソールから検索した情報を入力
    button = driver.find_elements_by_css_selector('.form-check')
    button[1].click()
    driver.find_element_by_class_name("form-control.form-search").send_keys(sub_word)
    driver.find_element_by_class_name("btn-search").click()
    
    count = 1
    is_break = False
    while not is_break:
        words = driver.find_elements_by_css_selector('.cntFdHead')
        for word in words:
            name = word.find_element_by_css_selector('.cntFdDcName')
            if name.text == '百科事典' or name.text == 'Wiktionary日本語版（日本語カテゴリ)' or name.text == '日本語表現辞典' or name.text == '日本語表現辞典' or name.text == '漢字辞典' or name.text =='Wiktionary日本語版（日本語カテゴリ）': 
                midashi = word.find_element_by_css_selector('.cntFdMidashi')
                title = midashi.get_attribute('title')
                word_list.append(title)
            if len(word_list) >= 50:
                is_break = True
                break
        next_link = 'https://www.weblio.jp/content_find/prefix/' + str(count) + '/' + sub_word
        driver.get(next_link)
        count += 1
        if len(driver.find_elements_by_id('cntFdWrp')) == 0:
            is_break = True
    
    return word_list

# end of line break

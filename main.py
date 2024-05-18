from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.get('https://web.rubika.ir/#/login')

sleep(5)

phone_number = ''

login_phone_number_input = driver.find_element(By.XPATH,'//*[@id="auth-pages"]/div/div[2]/div[1]/div/div[3]/div[3]/input[1]')

login_phone_number_input.send_keys(phone_number)

submit_login_button = driver.find_element(By.XPATH,'//*[@id="auth-pages"]/div/div[2]/div[1]/div/div[3]/button/div')
submit_login_button.click()

sleep(25)

chats = driver.find_elements(By.XPATH,'/html/body/app-root/div/div/div[1]/sidebar-container/div/sidebar-view/div/rb-chats/div[2]/div[1]/div/div[2]/div/ul/li')

while len(chats) != 1:

    driver.execute_script('arguments[0].scrollTo(0,1440)',driver.find_element(By.CSS_SELECTOR,'#folders-container > div'))

    sleep(3)

    chats = driver.find_elements(By.XPATH,'/html/body/app-root/div/div/div[1]/sidebar-container/div/sidebar-view/div/rb-chats/div[2]/div[1]/div/div[2]/div/ul/li')

    sleep(2)

    for index,single_chat in enumerate(chats):

        if index == 0: continue
        try:
            driver.execute_script("arguments[0].scrollIntoView();", single_chat)

        except:
            pass

        sleep(2)

        single_chat.click()

        sleep(2)

        try:
            open_chat_settings = driver.find_element(By.CSS_SELECTOR,'tab-conversation > div.sidebar-header.topbar > div.chat-info-container > div.chat-utils > div.btn-icon.rbico-more.btn-menu-toggle.rp')
            open_chat_settings.click()

            sleep(2)

            chat_settings_buttons = driver.find_elements(By.XPATH,'/html/body/div[2]/div')

            sleep(1)

            for single_chat_button in chat_settings_buttons:
                if single_chat_button.find_element(By.XPATH,'./span').text.find('ترک کانال') > -1:
                    single_chat_button.click()

                    sleep(2)

                    confirm_destroy_button = driver.find_element(By.CSS_SELECTOR,'.popup-buttons.popup-buttons-row .danger')

                    confirm_destroy_button.click()

                    break
            
                elif single_chat_button.find_element(By.XPATH,'./span').text.find('حذف مکالمه') > -1:
                    single_chat_button.click()

                    confirm_destroy_button = driver.find_element(By.CSS_SELECTOR,'div > app-confirm-custom > div.popup-buttons.popup-buttons-row > button.btn.danger.rp.btn-md-danger > div > div')

                    sleep(1)

                    confirm_destroy_button.click()

                    break
                else:
                    continue

        except:
            pass

        try:
            destroy_group_button = driver.find_element(By.CSS_SELECTOR,'tab-conversation > div.bubbles.scrolled-down.no-select.is-chat-input-hidden > div.message-fixed > div > div > div > div > button > div')

            destroy_group_button.click()

            sleep(2)

            confirm_destroy_button = driver.find_element(By.CSS_SELECTOR,'div > app-confirm-custom > div.popup-buttons.popup-buttons-row > button.btn.danger.rp > div')
            confirm_destroy_button.click()

            sleep(2)

            continue

        except:
            pass

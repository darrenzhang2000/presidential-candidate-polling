from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser


def get_driver_path():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['DRIVER_PATH']['path']


DRIVER_PATH = get_driver_path()

# we don't need the UI
options = Options()
options.headless = True

# wrong permissions: https://stackoverflow.com/questions/47148872/webdrivers-executable-may-have-wrong-permissions-please-see-https-sites-goo
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://projects.fivethirtyeight.com/polls/president-general/')
# print(driver.page_source)


rows = driver.find_elements_by_class_name('visible-row')
for r in rows:
    # note that element is singular because each tr only has one date
    date = r.find_element_by_class_name("date-wrapper").text
    print(date, '\n')


# pollster_links = driver.find_elements_by_class_name("pollster-container")

# for p in pollster_links:
#     #get child link
#     link = p.find_elements_by_tag_name("a")[1]
#     pollster = link.text
#     print(pollster, '\n')
# #     #great! at this point we've created a bunch of
# print(driver.page_source)

# print(pollster_links)
driver.quit()

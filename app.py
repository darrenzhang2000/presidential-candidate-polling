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
    # Note that element is singular 
    date = r.find_element_by_class_name("date-wrapper").text

    # The pollster container can have up to two links. One for the grade, if it exists,
    # and one for the pollster name. We want the latter.
    pollster_container = r.find_element_by_class_name("pollster-container")
    pollster_links = pollster_container.find_elements_by_tag_name("a")
    pollster_name = pollster_links[-1].text # Accesses last element of the link array
    
    sample_size = r.find_element_by_class_name("sample").text
    
    leader = r.find_element_by_class_name("leader").text

    net = r.find_element_by_class_name("net").text

    values = r.find_elements_by_class_name("value")

    # If the other value is hidden by the "more" button
    if len(values) == 1:   
        next_sibling = r.find_element_by_xpath("following-sibling::tr[@class='expandable-row']")
        value = next_sibling.find_element_by_class_name("value")
        values.append(value)
    
    # For some reason using .text doesn't always work, so I'm using .get_attribute instead
    trump_fav = values[0].find_element_by_class_name("heat-map").get_attribute('innerHTML')
    biden_fav = values[1].find_element_by_class_name("heat-map").get_attribute('innerHTML')

driver.quit()

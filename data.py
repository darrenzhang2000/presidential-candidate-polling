from bs4 import BeautifulSoup
import requests

def scrape_poll_data(): #ADDED THIS
    pollster_data_array = [] #ADDED THIS
    
    URL = 'https://projects.fivethirtyeight.com/polls/president-general/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    rows = soup.find_all(class_='visible-row')
    for r in rows:
        date = r.find(class_='date-wrapper').text

        # The pollster container can have up to two links. One for the grade, if it exists,
        # and one for the pollster name. We want the latter.
        pollster_container = r.find(class_="pollster-container")
        pollster_links = pollster_container.find_all("a")
        # Accesses last element of the link array
        pollster_name = pollster_links[-1].text

        sample_size = r.find(class_="sample").text

        leader = r.find(class_="leader").text

        net = r.find(class_="net").text

        # Getting the percent favorable for Trump and Biden
        values = r.find_all(class_="value")
        # If the other value is hidden by the "more" button
        if len(values) == 1:
            next_sibling = r.findNext("tr")
            value = next_sibling.find(class_="value")
            values.append(value)

        trump_fav = values[0].find(class_="heat-map").text
        biden_fav = values[1].find(class_="heat-map").text

        pollster_data = { 
            "date": date,
            "pollster_name": pollster_name,
            "sample_size": sample_size,
            "leader": leader,
            "net": net,
            "trump_fav": trump_fav,
            "biden_fav": biden_fav
        }

        pollster_data_array.append(pollster_data)
    return pollster_data_array

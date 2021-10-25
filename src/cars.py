# from pprint import pprint
from requests import get
from bs4 import BeautifulSoup

from requests.models import Response

# In Google: what is my user agent
HEADERS = {
        "user-agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/95.0.4638.54 Safari/537.36")
    }


def get_porsche(city:str="kansascity", model: str="porsche%20944") -> Response:
    """GET current Craigslist porsche 944 postings"""

    if model:
        model = build_search(model)
    url = f"https://{city}.craigslist.org/d/cars-trucks/search/cta?query={model}&sort=rel"
    response = get(url, headers=HEADERS)
    response.raise_for_status()
    return response

def build_search(model: str) -> str:
    """Build search for craigslist"""
    car = ""
    search = model.split()
    if len(search) <= 1:
        pass
    else:
        for item in range(len(search) - 1):
            car = car + search[item] + "%20"
    return car + search[-1]

def get_soup(response: Response) -> list:
    """Parse the reponse into a nested list"""
    _cars = []
    html_soup = BeautifulSoup(response.text, "html.parser")
    posts = html_soup.find_all("li", class_= "result-row")  # Find all porsche postings
    for post in posts:
        url = post.find("a", class_="result-title hdrlnk")['href']
        _cars.append(
            {
                "datelisted": post.find("time", class_= "result-date")['datetime'],
                "price": post.a.text.strip(),
                "title": post.find("a", class_="result-title hdrlnk").text,
                "url": url,
                "location": url.split("https://")[1].split(".")[0],  # Splits url at 'https://' and the 1st . after city
            }
        )
    cars = remove_dupes(_cars)
    return cars

def remove_dupes(car_list):
    """Remove duplicate dicts from list"""
    x = set()
    cars = []
    for i in car_list:
        if i['title'] not in x:
            x.add(i['title'])
            cars.append(i)
        else:
            continue
    return cars


if __name__ == "__main__":
    response = get_porsche()
    x = get_soup(response)

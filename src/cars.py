from requests import get
from bs4 import BeautifulSoup
from pprint import pprint

from requests.models import Response


def get_porsche(city:str="kansascity", model: str="porsche%20944") -> Response:
    """GET current Craigslist porsche 944 postings"""
    if model:
        model = build_search(model)
    url = f"https://{city}.craigslist.org/d/cars-trucks/search/cta?query={model}&sort=rel"
    return get(url)

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
    cars = []
    html_soup = BeautifulSoup(response.text, "html.parser")
    posts = html_soup.find_all("li", class_= "result-row")  # Find all porsche postings
    for post in posts:
        url = post.find("a", class_="result-title hdrlnk")['href']
        cars.append(
            {
                "datelisted": post.find("time", class_= "result-date")['datetime'],
                "price": post.a.text.strip(),
                "title": post.find("a", class_="result-title hdrlnk").text,
                "url": url,
                "location": url.split("https://")[1].split(".")[0],  # Splits url at 'https://' and the 1st . after city
            }
        )
    return cars


if __name__ == "__main__":
    response = get_porsche()
    pprint(get_soup(response), indent=2)

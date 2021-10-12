# Create free tier aws server Do it from a free tier aws server and see how much you can do.
# Update me via webex
# Find one that has Cisco Gear Posted
# https://towardsdatascience.com/get-your-own-data-building-a-scalable-web-scraper-with-aws-654feb9fdad7
# https://towardsdatascience.com/web-scraping-craigslist-a-complete-tutorial-c41cea4f4981
# https://towardsdatascience.com/python-type-annotations-and-why-you-should-use-them-6f647c6b4e9c
from requests import get
from bs4 import BeautifulSoup
from pprint import pprint

from requests.models import Response


MO_CITIES = ["ames","cedar rapids","columbia","des moines","fayetteville","fort dodge",
             "fort smith","grand island","iowa city","joplin","kirksville","lake of ozarks",
             "lawrence","lincoln","manhattan","northwest ok","omaha","salina","sioux city",
             "southeast ia","southeast ks","springfield","stillwater","st joseph","st louis",
             "topeka","tulsa","waterloo","western il","wichita","kansascity",]


def get_porsche(city:str="kansascity") -> Response:
    """GET current Craigslist porsche 944 postings"""
    return get(f"https://{city}.craigslist.org/search/sss?query=porsche%20944&sort=rel")

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

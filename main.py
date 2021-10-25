#!/usr/bin/env python
"""
Craigslist APP that searches for cars and adds them to a database
"""
# from pprint import pprint
from  src import cars
from src.cardb import CarsDb


def main(location: str='kansascity', cities: bool=False) -> None:
    """
    Print GET Porsche request from Craigslist results
    Args:
        cities (bool): (Optional) list of 413 cities
        location (str): city used for craigslist search (default: kansascity)

    Return: None
    """
    car_list = []
    if cities:
        location = ''
        city_list = get_cities()
        for city in city_list:
            response = cars.get_porsche(city=city)
            car = cars.get_soup(response)
            if len(car) > 0:
                car_list.append(cars.get_soup(response))
    else:
        response = cars.get_porsche()
        car = cars.get_soup(response)
        car_list.append(car)
    add_to_db(car_list)
    results = get_pandas(location)
    return results

def get_cities() -> list:
    """
    Open Craigslist cities from text
    Args:
        None

    Return: list
    """
    results = []
    with open('src/craigslist_cities.txt', 'r', encoding='utf8') as file:
        for line in file:
            results.append(line.strip())
    return results

def add_to_db(car_list: list) -> dict:
    """
    Open Craigslist cities from text
    Args:
        None

    Return: list
    """
    db = CarsDb()  # pylint: disable=invalid-name
    db.create_table()
    for _cars in car_list:
        for car in _cars:
            db.add_cars(car)
    db.commit()
    db.close()

def get_db_entries(location: str='') -> list:
    """
    GET CAR db entries
    Args:
        location (str): (Optional) craigslist porsche location

    Return: list
    """
    db = CarsDb()  # pylint: disable=invalid-name
    results = db.get_cars(location)
    db.commit()
    db.close()
    return results

def get_pandas(location: str='') -> 'pandas.core.frame.DataFrame':
    """
    GET CAR pandas query
    Args:
        location (str): (Optional) craigslist porsche location

    Return: pandas.core.frame.DataFrame
    """
    db = CarsDb()  # pylint: disable=invalid-name
    results = db.get_pandas(location)
    db.commit()
    db.close()
    return results.set_index('id')

def print_cities() -> None:
    """
    Prints a menu of number cities.
    """
    city_list = get_cities()
    i = 1
    for a,b,c,d,e in zip(city_list[::5], city_list[1::5], city_list[2::5], city_list[3::5], city_list[4::5]):
        a = str(i) + f".{a}"
        i += 1
        b = str(i) + f".{b}"
        i += 1
        c = str(i) + f".{c}"
        i += 1
        d = str(i) + f".{d}"
        i += 1
        e = str(i) + f".{e}"
        i += 1
        print("{:<20}{:<20}{:<20}{:<20}{:<}".format(a,b,c,d,e))


if __name__ == "__main__":
    import argparse
    from rich.console import Console
    console = Console()
    parser = argparse.ArgumentParser(description="To scan ALL craigslist cities:")
    parser.add_argument("--all", help="Optional argument to scan all craigslist cities.",
                        action='store_true')
    parser.add_argument("--city", help="Optional argument to select city.",
                        action='store_true')
    args = parser.parse_args()
    if args.city:
        while True:
            cities = get_cities()
            print("\n", "\t" * 3, "LATEST LIST OF CRAIGSLIST CITIES")
            print_cities()
            print()
            while True:
                try:
                    user_input = int(input("Select city number to search for porsche: "))
                    try:
                        city = cities[user_input-1]
                        break
                    except IndexError:
                        print("Please enter a number between 1 and 410.\n")
                except ValueError:
                    print("Please enter a valid number.\n")
            print(f"\nHere are the results for {cities[user_input-1]}:\n")
            break
        console.print(main(location=city))
    else:
        if args.all:
            console.print(main(cities=True))
        else:
            console.print(main(cities=False))

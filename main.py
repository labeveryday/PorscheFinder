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
    if cities:
        results = get_db_entries()
    else:
        results = get_db_entries(location)
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
        location (str): craigslist porsche location

    Return: list
    """
    db = CarsDb()  # pylint: disable=invalid-name
    results = db.get_cars(location)
    db.commit()
    db.close()
    return results


if __name__ == "__main__":
    main(cities=False)
    # pprint(get_db_entries('cleveland'))

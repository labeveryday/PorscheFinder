import src.cars as cars
from src.cardb import CarsDb
from pprint import pprint


def main() -> None:
    response = cars.get_porsche()
    car_list = cars.get_soup(response)
    db = CarsDb()
    db.create_table()
    for car in car_list:
        db.add_cars(car)
    pprint(db.get_cars())
    db.close()


if __name__ == "__main__":
    main()

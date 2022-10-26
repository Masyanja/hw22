# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, city_population, room):
        self.city_population = city_population
        self.room = room

    def get_person_room(self):
        return self.room

    def get_city_population(self):
        return self.city_population

if __name__== '__main__':
    person = Person(4000, 34)
    print(person.get_person_room())
    print(person.get_city_population())
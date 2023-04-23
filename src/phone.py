from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        if number_of_sim <= 0:
            ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        super().__init__(name, price, quantity)
        self.__name = name
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
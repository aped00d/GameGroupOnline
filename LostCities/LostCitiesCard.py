from LostCities.LostCitiesCardSuit import LostCitiesCardSuit
from LostCities.LostCitiesCardValue import LostCitiesCardValue


class LostCitiesCard:

    def __init__(self):
        self.suit = ""
        self.value = ""

    def __init__(self, suit: LostCitiesCardSuit, value: LostCitiesCardValue):
        if not isinstance(suit, LostCitiesCardSuit):
            raise TypeError("The suit submitted was not a lost cities card suit")
        if not isinstance(value, LostCitiesCardValue):
            raise TypeError("The value submitted was not a lost cities card value")
        self.suit = suit
        self.value = value

    def __eq__(self, other):
        return isinstance(other, LostCitiesCard) and self.suit == other.suit and self.value == other.value

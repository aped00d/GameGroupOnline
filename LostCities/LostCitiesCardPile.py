from LostCities.LostCitiesCardSuit import LostCitiesCardSuit
from LostCities.LostCitiesCard import LostCitiesCard


class LostCitiesCardPile:
    def __init__(self, suit: LostCitiesCardSuit):
        self.cards = []
        self.suit = suit

    def validate_card(self, card):
        if not isinstance(card, LostCitiesCard):
            raise TypeError("Cannot add non Lost Cities Card")

        if card.suit != self.suit:
            raise TypeError(f"Cannot add card with suit {card.suit} to tableau with suit {self.suit}")

    def get_top_card(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None

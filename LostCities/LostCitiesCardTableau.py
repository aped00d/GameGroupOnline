from LostCities.LostCitiesCard import LostCitiesCard
from LostCities.LostCitiesCardSuit import LostCitiesCardSuit

class LostCitiesCardTableau:

    def __init__(self, suit: LostCitiesCardSuit):
        self.cards = []
        self.suit = suit

    def add_card(self, card: LostCitiesCard):
        if not isinstance(card, LostCitiesCard):
            raise TypeError("Cannot add non Lost Cities Card")

        if card.suit != self.suit:
            raise TypeError(f"Cannot add card with suit {card.suit} to tableau with suit {self.suit}")

        if self.get_top_card() is not None and card.value.value < self.get_top_card().value.value:
            raise TypeError(
                f"Cannot add card with value {card.value}, card must be greater than {self.get_top_card().value}")

        self.cards.append(card)

    @property
    def get_total_value(self):
        if len(self.cards) == 0:
            return 0

        multiplier = 1
        total = -20
        bonus = 0

        for card in self.cards:
            if card.value.value == 0:
                multiplier += 1
            else:
                total += card.value.value

        if len(self.cards) >= 8:
            bonus = 20

        return (total * multiplier) + bonus

    def get_top_card(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None

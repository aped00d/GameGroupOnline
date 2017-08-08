from LostCities.LostCitiesCard import LostCitiesCard
from LostCities.LostCitiesDrawPile import LostCitiesDrawPile


class LostCitiesDiscardPile(LostCitiesDrawPile):

    def add_card(self, card: LostCitiesCard):
        self.validate_card(card)
        self.cards.append(card)

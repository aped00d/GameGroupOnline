from LostCities.LostCitiesCardPile import LostCitiesCardPile


class LostCitiesDrawPile(LostCitiesCardPile):

    def draw_card(self):
        return self.cards.pop()
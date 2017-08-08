import unittest
from LostCities.LostCitiesCard import LostCitiesCard
from LostCities.LostCitiesCardTableau import LostCitiesCardTableau
from LostCities.LostCitiesCardSuit import LostCitiesCardSuit
from LostCities.LostCitiesCardValue import LostCitiesCardValue


__author__ = 'davidh'


class LostCitiesCardTableauTests(unittest.TestCase):

    def test_add_card(self):
        card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.EIGHT)
        tableau = LostCitiesCardTableau(LostCitiesCardSuit.RED)
        tableau.add_card(card)
        self.assertEqual(card, tableau.get_top_card(),
                         f"The top card of the tableau is not {card.suit} {card.value} as expected")

    def test_cannot_add_card_with_wrong_suit(self):
        card = LostCitiesCard(LostCitiesCardSuit.BLUE, LostCitiesCardValue.EIGHT)
        tableau = LostCitiesCardTableau(LostCitiesCardSuit.RED)
        with self.assertRaises(TypeError):
            tableau.add_card(card)

    def test_cannot_add_card_with_lower_value(self):
        card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.TEN)
        tableau = LostCitiesCardTableau(LostCitiesCardSuit.RED)
        tableau.add_card(card)
        lower_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.NINE)
        with self.assertRaises(TypeError):
            tableau.add_card(lower_card)

    def test_cannot_add_a_none_card(self):
        card = "red 9"
        tableau = LostCitiesCardTableau(LostCitiesCardSuit.RED)
        with self.assertRaises(TypeError):
            tableau.add_card(card)

    def test_top_card_is_highest(self):
        first_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.TWO)
        second_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.THREE)
        third_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.FOUR)
        tableau = LostCitiesCardTableau(LostCitiesCardSuit.RED)
        tableau.add_card(first_card)
        tableau.add_card(second_card)
        tableau.add_card(third_card)
        self.assertEqual(third_card, tableau.get_top_card(),
                         f"Top card was not {third_card.suit} {third_card.value} as expected")

    def test_tableau_total(self):
        first_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.TWO)
        second_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.THREE)
        third_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.FOUR)
        tableau = LostCitiesCardTableau(LostCitiesCardSuit.RED)
        tableau.add_card(first_card)
        tableau.add_card(second_card)
        tableau.add_card(third_card)
        self.assertEqual(-20 + 2 + 3 + 4, tableau.get_total_value)

    def test_tableau_total_with_bonus(self):
        first_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.TWO)
        second_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.THREE)
        third_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.FOUR)
        fourth_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.FIVE)
        fifth_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.SIX)
        sixth_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.SEVEN)
        seventh_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.EIGHT)
        eighth_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.NINE)
        tableau = LostCitiesCardTableau(LostCitiesCardSuit.RED)
        tableau.add_card(first_card)
        tableau.add_card(second_card)
        tableau.add_card(third_card)
        tableau.add_card(fourth_card)
        tableau.add_card(fifth_card)
        tableau.add_card(sixth_card)
        tableau.add_card(seventh_card)
        tableau.add_card(eighth_card)
        self.assertEqual(-20 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 20, tableau.get_total_value)

    def test_tableau_total_with_single_investment(self):
        investment_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.INVESTMENT)
        first_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.TWO)
        second_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.THREE)
        third_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.FOUR)
        tableau = LostCitiesCardTableau(LostCitiesCardSuit.RED)
        tableau.add_card(investment_card)
        tableau.add_card(first_card)
        tableau.add_card(second_card)
        tableau.add_card(third_card)
        self.assertEqual((-20 + 2 + 3 + 4) * 2, tableau.get_total_value)

    def test_tableau_total_with_only_investment(self):
        first_investment_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.INVESTMENT)
        second_investment_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.INVESTMENT)
        third_investment_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.INVESTMENT)
        tableau = LostCitiesCardTableau(LostCitiesCardSuit.RED)
        tableau.add_card(first_investment_card)
        tableau.add_card(second_investment_card)
        tableau.add_card(third_investment_card)
        self.assertEqual(-20 * 4, tableau.get_total_value)


    def test_tableau_total_with_bonus_and_investment(self):
        investment_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.INVESTMENT)
        first_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.TWO)
        second_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.THREE)
        third_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.FOUR)
        fourth_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.FIVE)
        fifth_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.SIX)
        sixth_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.SEVEN)
        seventh_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.EIGHT)
        tableau = LostCitiesCardTableau(LostCitiesCardSuit.RED)
        tableau.add_card(investment_card)
        tableau.add_card(first_card)
        tableau.add_card(second_card)
        tableau.add_card(third_card)
        tableau.add_card(fourth_card)
        tableau.add_card(fifth_card)
        tableau.add_card(sixth_card)
        tableau.add_card(seventh_card)
        self.assertEqual(((-20 + 2 + 3 + 4 + 5 + 6 + 7 + 8) * 2) + 20, tableau.get_total_value)

    def test_tableau_add_multiple_investments(self):
        first_investment_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.INVESTMENT)
        second_investment_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.INVESTMENT)
        tableau = LostCitiesCardTableau(LostCitiesCardSuit.RED)
        tableau.add_card(first_investment_card)
        tableau.add_card(second_investment_card)
        self.assertEqual(second_investment_card, tableau.get_top_card())
        self.assertEqual(-20 * 3, tableau.get_total_value)

    def test_tableau_total_with_multiple_investments(self):
        first_investment_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.INVESTMENT)
        second_investment_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.INVESTMENT)
        first_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.TWO)
        second_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.THREE)
        third_card = LostCitiesCard(LostCitiesCardSuit.RED, LostCitiesCardValue.FOUR)
        tableau = LostCitiesCardTableau(LostCitiesCardSuit.RED)
        tableau.add_card(first_investment_card)
        tableau.add_card(second_investment_card)
        tableau.add_card(first_card)
        tableau.add_card(second_card)
        tableau.add_card(third_card)
        self.assertEqual((-20 + 2 + 3 + 4) * 3, tableau.get_total_value)

    if __name__ == '__main__':
        unittest

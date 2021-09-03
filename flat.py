class Bill:
    """
    Object that contains data about a bill,
    such as total amount & period,

    :param amount: The bill amount in pence
    :param period: The period of the bill
    :return
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a Flatmate person who lives in the flat
    and pays their share of the bill.

    :param name: The Flatmate's name
    :param days_in_house: The number of days in a given period the Flatmate spent in the house
    :return
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        weight = self.days_in_house / (self.days_in_house + flatmate.days_in_house)
        return round(bill.amount * weight, 2)
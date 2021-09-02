import os
import webbrowser

from fpdf import FPDF


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


class PdfReport:
    """
    Creates a PDF report of the bill

    :param filename: The name of the generated PDF file
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, bill, flatmate1, flatmate2):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add icon
        pdf.image(name="files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        # insert icon here
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=18, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=200, h=40, txt=bill.period, border=0, ln=1)

        # Insert name label & amount to pay
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=25, txt=f"{flatmate1.name}:", border=0)
        pdf.cell(w=200, h=25, txt=f"£{flatmate1.pays(bill, flatmate2)}", border=0, ln=1)
        pdf.cell(w=100, h=25, txt=f"{flatmate2.name}:", border=0)
        pdf.cell(w=200, h=25, txt=f"£{flatmate2.pays(bill, flatmate1)}", border=0, ln=1)

        # Generate & open the file
        pdf.output(self.filename)
        webbrowser.open(f"file://{os.path.realpath(self.filename)}")


if __name__ == "__main__":
    bill_amount = float(input("Enter bill amount: "))
    bill_period = input("Enter the bill period: ")
    month_bill = Bill(amount=bill_amount, period=bill_period)

    flatmate1_name = input("Enter the name of the first flatmate: ")
    flatmate1_days = int(input(f"How many days did {flatmate1_name} spend in house? "))
    flatmate2_name = input("Enter the name of the second flatmate: ")
    flatmate2_days = int(input(f"How many days did {flatmate2_name} spend in house? "))
    flatmate1 = Flatmate(name=flatmate1_name, days_in_house=flatmate1_days)
    flatmate2 = Flatmate(name=flatmate2_name, days_in_house=flatmate2_days)

    print(f"{flatmate1_name} pays: £", flatmate1.pays(month_bill, flatmate2))
    print(f"{flatmate2_name} pays: £", flatmate2.pays(month_bill, flatmate1))

    pdf_report = PdfReport(filename="bill.pdf")
    pdf_report.generate(bill=month_bill, flatmate1=flatmate1, flatmate2=flatmate2)

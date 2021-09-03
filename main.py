from flat import Bill, Flatmate
from reports import PdfReport

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

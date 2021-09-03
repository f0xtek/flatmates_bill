import os
import webbrowser

from fpdf import FPDF


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
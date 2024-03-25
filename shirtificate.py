from fpdf import FPDF


def get_name():
    return input("Enter your name: ")


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 32)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 30, "CS50 Shirtificate", align="C")
        self.ln(20)


pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 20)
pdf.image("shirtificate.png", 5, 50, 200)
pdf.set_text_color(255, 255, 255)
pdf.cell(1, 60, new_x="LMARGIN", new_y="NEXT", align="C")
pdf.cell(w=40)
pdf.cell(
    110,
    50,
    f"{get_name()} took CS50",
    align="C",
)
pdf.output("shirtificate.pdf")

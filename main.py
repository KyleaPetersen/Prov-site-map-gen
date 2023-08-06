import os
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader
# from coordinates import *

#Creates new PDF marking locations
def generate(unit_coords, dumpster, mailbox):
    # Get the absolute path of the script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Create the watermark from an image
    watermark_file = os.path.join(script_directory, 'watermark.pdf')
    c = canvas.Canvas(watermark_file)

    # Circle apartment and label is
    c.circle(unit_coords[0], unit_coords[1], r = 5, fill = 1)
    c.line((unit_coords[0] - 10), unit_coords[1], 90, unit_coords[1])
    c.drawRightString(86, unit_coords[1], "Your Apartment")

    # Circle Mailbox
    c.circle(mailbox[0], mailbox[1], r = 4, fill = 1)
    c.line((mailbox[0] - 10), mailbox[1], 90, mailbox[1])
    c.drawRightString(86, mailbox[1], "Your Mailbox")

    #circle nearest dumpster
    c.circle(dumpster[0], dumpster[1], r = 4)
    c.save()

    # Open the original PDF
    original_pdf_file = os.path.join(script_directory, 'basic.pdf')
    original_pdf = PdfReader(open(original_pdf_file, 'rb'))

    # Open the watermark PDF
    watermark_pdf = PdfReader(open(watermark_file, 'rb'))

    # Create a new PDF to store the watermarked content
    output_pdf = PdfWriter()

    # Overlay the watermark on each page of the original PDF
    for page_num in range(len(original_pdf.pages)):
        page = original_pdf.pages[page_num]
        page.merge_page(watermark_pdf.pages[0])
        output_pdf.add_page(page)  # Corrected line

    # Save the watermarked PDF to a new file
    with open('watermarked_output.pdf', 'wb') as f:
        output_pdf.write(f)
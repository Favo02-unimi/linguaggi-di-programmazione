# crop each page of a pdf document into 4 pages
# usage: python slide_cutter.py <input.pdf> <output.pdf>
# requirements: PyPDF2 (pip install PyPDF2)

import PyPDF2
import sys

def crop_pdf(input, output):

  with open(input, "rb") as input_pdf:
    reader = PyPDF2.PdfReader(input_pdf)
    writer = PyPDF2.PdfWriter()

    for page in reader.pages:

      width = page.mediabox.width
      height = page.mediabox.height

      page1 = (height / 2, width / 2, height, 0)
      page2 = (height / 2, width, height, width / 2)
      page3 = (0, width / 2, height / 2, 0)
      page4 = (0, width, height / 2, width / 2)

      pages = [page1, page2, page3, page4]

      for coords in pages:
        page.cropbox.top = coords[0]
        page.cropbox.right = coords[1]
        page.cropbox.bottom = coords[2]
        page.cropbox.left = coords[3]
        writer.add_page(page)

    with open(output, "wb") as output_pdf:
      writer.write(output_pdf)

input = sys.argv[1]
output = sys.argv[2]
print("Cropping", input, "to", output)

crop_pdf(input, output)

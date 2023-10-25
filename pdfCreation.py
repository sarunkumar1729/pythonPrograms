from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a PDF file
c = canvas.Canvas("example.pdf", pagesize=letter)

# Set font and font size
c.setFont("Helvetica", 12)

# Add text to the PDF
c.drawString(100, 750, "Hello, this is a PDF created with Python!")
c.drawString(100, 730, "You can add text, shapes, and more.")

# Save the PDF
c.showPage()
c.save()

print("PDF created successfully.")

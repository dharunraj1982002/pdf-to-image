# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
images = convert_from_path('goa2.pdf',500,poppler_path=r'C:\Program Files\poppler-0.68.0_x86\bin')

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')

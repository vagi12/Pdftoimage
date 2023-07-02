import os
import fitz

def convert_pdf_to_images(pdf_file, output_folder, output_format='JPEG'):
    doc = fitz.open(pdf_file)
    output_images = []

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(doc.page_count):
        page = doc.load_page(i)
        pix = page.get_pixmap()
        output_filename = f'page_{i}.{output_format.lower()}'
        output_filepath = os.path.join(output_folder, output_filename)
        pix.save(output_filepath, output_format)
        output_images.append(output_filepath)

    return output_images

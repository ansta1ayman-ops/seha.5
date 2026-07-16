import os
import fitz  # PyMuPDF


class PDFEngine:

    def __init__(self):
        os.makedirs("output", exist_ok=True)

    def create_pdf(self, template_path, output_name):
        """
        إنشاء نسخة جديدة من النموذج
        """
        doc = fitz.open(template_path)

        output_path = os.path.join("output", output_name)

        doc.save(output_path)
        doc.close()

        return output_path

    def write_text(
        self,
        pdf_path,
        page_number,
        x,
        y,
        text,
        font_size=12,
        color=(0, 0, 0),
    ):
        """
        كتابة نص داخل PDF
        """

        doc = fitz.open(pdf_path)

        page = doc[page_number]

        page.insert_text(
            (x, y),
            text,
            fontsize=font_size,
            color=color,
        )

        doc.saveIncr()

        doc.close()

        return pdf_path

    def page_count(self, pdf_path):
        doc = fitz.open(pdf_path)
        count = len(doc)
        doc.close()
        return count

    def get_size(self, pdf_path, page_number=0):
        doc = fitz.open(pdf_path)
        page = doc[page_number]
        rect = page.rect
        doc.close()
        return rect.width, rect.height


pdf_engine = PDFEngine()
import PyPDF2

class PDFProcessor:
    def process_pdf(self, file):
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        text = ''
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        # Perform any additional preprocessing steps on the text
        text = self.clean_text(text)

        # Return the list of passages
        return text

    def clean_text(self, text):
        # Remove unwanted characters, normalize text, etc.
        cleaned_text = text.replace('\n', ' ').replace('\r', '').strip()
        return cleaned_text
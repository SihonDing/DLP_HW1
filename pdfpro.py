import importlib, sys
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage
from pdfminer.converter import PDFPageAggregator
import re
importlib.reload(sys)
sys.getdefaultencoding()

class PDF_Parser:
    # Set the file path
    def init1(self, pdf_path):
        self.pdf_path = pdf_path

    def init2(self, save_path):
        self.save_path = save_path
        print(save_path)

    def Parsing(self):
        # Open a PDF file.
        fp = open(self.pdf_path, 'rb')
        # Create a PDF parser object associated with the file object.
        parser = PDFParser(fp)
        # Create a PDF document object that stores the document structure.
        # Supply the password for initialization.
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        document = PDFDocument(parser)
        # Process each page contained in the document.
        text_content = []
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            layout = device.get_result()
            for lt_obj in layout:
                if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                    text_content.append(lt_obj.get_text())
                else:
                    pass
        # Each element in text_content stores a line of words.
        total_text = ''.join(text_content).replace("\n", "")
        # Parse the reference from the strings.
        # file = open(self.save_path, "w", encoding='utf-8')
        p = re.compile('\[\d+\]\s[A-Z]\D+\W\s[^\[]*')
        m = p.findall(total_text)
        m.sort(key=self.list_sort)
        print(len(m))
        for i in range(len(m)):
            m[i] = re.sub('[-]', '', m[i])
        return m

    def list_sort(self, str):
        # Sort the references.
        index1 = str.index('[')
        index2 = str.index(']')
        return int(str[index1 + 1:index2])

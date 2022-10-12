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
        # text_content 中每一个元素存储了一行文字
        total_text = ''.join(text_content).replace("\n", "")
        # 从字符串中解析出参考文献
        # file = open(self.save_path, "w", encoding='utf-8')
        p = re.compile('\[\d+\]\s[A-Z]\D+\W\s[^\[]*')
        m = p.findall(total_text)
        m.sort(key=self.list_sort)
        print(len(m))
        for i in range(len(m)):
            m[i] = re.sub('[-]', '', m[i])
        return m
    def list_sort(self, str):
        index1 = str.index('[')
        index2 = str.index(']')
        return int(str[index1 + 1:index2])
# if __name__ == 'main':
#     # Open a PDF file.
#     fp = open("He_Deep_Residual_Learning_CVPR_2016_paper.pdf", 'rb')
#     # Create a PDF parser object associated with the file object.
#     parser = PDFParser(fp)
#     # Create a PDF document object that stores the document structure.
#     # Supply the password for initialization.
#     rsrcmgr = PDFResourceManager()
#     laparams = LAParams()
#     device = PDFPageAggregator(rsrcmgr, laparams=laparams)
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     document = PDFDocument(parser)
#     # Process each page contained in the document.
#     text_content = []
#     for page in PDFPage.create_pages(document):
#         interpreter.process_page(page)
#         layout = device.get_result()
#         for lt_obj in layout:
#             if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
#                 text_content.append(lt_obj.get_text())
#             else:
#                 pass
#
#     # text_content 中每一个元素存储了一行文字
#     total_text = ''.join(text_content).replace("\n", "")
#     # 从字符串中解析出参考文献
#     file = open("save_file.txt", "w", encoding='utf-8')
#     # p = re.compile('\[\d+\][^\[\]]*\d\.')
#     p = re.compile('\[\d+\]\s[A-Z]\D+\W\s[^\[]*')
#     # p = re.compile('\[\d+\]\s[A-Z]\D+\W\s.*?\D')
#     m = p.findall(total_text)
#     # m.sort(key=list_sort)
#     print(type(m))
#     for i in m:
#         # print i
#         # print(i[5])
#         # if i.startswith("["):
#             file.write(str(i))
#             file.write("\n")
#     file.close()
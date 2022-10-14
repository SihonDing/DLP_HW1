import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename, askdirectory
from webAPI import API
from pdfpro import PDF_Parser

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

    def init(self, web=None, pdf=None):
        self.web = web
        self.pdf = pdf
        self.creat_widgets()

    def creat_widgets(self):
        global img
        self.master.geometry('750x500+300+200')
        self.master.resizable(False, False)
        self.master.title('PDF Parser')
        load = Image.open('USTCex.jpg')
        load = load.resize((150, 150))
        img = ImageTk.PhotoImage(load)
        label1 = tk.Label(self.master, image=img)
        label1.place(width=150, height=150, x=100, y=50)
        label0 = tk.Label(self.master, text='论文解析器', fg='red', font=('华文新魏',25))
        label0.place(width=200, height=100, x=80, y=200)
        # label0.pack()
        self.txt1 = tk.Text(self.master)
        self.txt1.place(relx=0.5, rely=0, height=500)
        self.txt2 = tk.Text(self.master)
        self.txt2.place(relx=0.5, rely=0.5)
        btn1 = tk.Button(self.master, text='新增解析文件', command=self.set_paper_path)
        btn1.place(x=20, y=300)
        self.txt3 = tk.Text(self.master)
        self.txt3.place(x=120, y=300, width=230, height=30)
        btn2 = tk.Button(self.master, text='设置下载路径', command=self.set_download_path)
        btn2.place(x=20, y=350)
        self.txt4 = tk.Text(self.master)
        self.txt4.place(x=120, y=350, width=230, height=30)
        btn3 = tk.Button(self.master, text='开始解析!', command=self.pdf_process)
        btn3.place(x=50, y=420, width=100, height=30)
        btn4 = tk.Button(self.master, text='爬取论文!',command=self.get_from_net)
        btn4.place(x=200, y=420, width=100, height=30)

    def pdf_process(self):
        self.papers = self.pdf.Parsing()
        print(self.papers)
        print(type(self.papers))
        for i in self.papers:
            i = i + '\n'
            self.txt1.insert('end', i)

    def get_from_net(self):
        for i in self.papers:
            self.backinfo = self.web.gfweb(i)
            self.backinfo = self.backinfo + '\n'
            self.txt2.insert('end', self.backinfo)

    def set_paper_path(self):
        self.paper_path = askopenfilename()
        if self.paper_path != '':
            self.txt3.insert('end', self.paper_path)
            self.pdf.init1(self.paper_path)

    def set_download_path(self):
        self.download_path = askdirectory()
        if self.download_path != '':
            self.txt4.insert('end', self.download_path)
            self.pdf.init2(self.download_path)
            self.web.init(self.download_path)


if __name__ == "__main__":
    web = API()
    pdf = PDF_Parser()
    root = tk.Tk()
    app = Application(master=root)
    app.init(web=web, pdf=pdf)
    app.mainloop()


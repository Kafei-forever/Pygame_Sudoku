import tkinter.messagebox,os
dir_list=os.listdir("./sudoku_file")
class load_date():
    def __init__(self):
        self.i=0
        self.data = []
        self.pos = ()
        self.available=True
    def load(self):
        try:
            open("./sudoku_file/"+dir_list[self.i])
        except IOError:
            tkinter.messagebox.showwarning("Warning","Can't find data file")
            self.available=False
        else:
            for line in open("./sudoku_file/"+dir_list[self.i]):
                line = line[:-1]
                pos = eval(line)
                self.data.append(pos)
                # print(data)
    def reload(self):
        if self.i<1:
            self.i+=1
            self.data = []
            self.load()
ld=load_date()



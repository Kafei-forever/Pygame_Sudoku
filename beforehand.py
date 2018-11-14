import tkinter.messagebox,os
dir_list=os.listdir("./sudoku_file")
#print(dir_list)
class load_date():
    def __init__(self):
        self.i=0
        self.data = []
        self.pos = ()
        self.available=True
    def load(self,stage):
        self.data.clear()
        self.i=stage
        try:
            a=open("./sudoku_file/"+dir_list[self.i])
            a.close()
        except IndexError or OSError:
            tkinter.messagebox.showwarning("Warning","Can't find data file")
            self.available=False
        else:
            for line in open("./sudoku_file/"+dir_list[self.i]):#通过迭代访问每一行
                line = line[:-1]
                pos = eval(line)  # 用来执行一个字符串表达式，并返回表达式的值。
                self.data.append(pos)
                # txt文本最后一行要加上一个空格 因为最后一行默认最后没有空格 会截掉。
                # print(data)
    def reload(self):
        if self.i<=4:
            self.i+=1
            self.data.clear()
            self.load(self.i)
        else:
            pass
ld=load_date()
#print(ld.data)


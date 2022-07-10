from tkinter import *
from tkinter import ttk
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\unit-converter\\')

root = Tk()
root.title('Unit Converter')
x = int(root.winfo_screenwidth() // 2)
y = int(root.winfo_screenheight() * 0.2)
x, y = str(x), str(y)
root.geometry(f'350x350+{x}+{y}')
root.resizable(False, False)
root.iconbitmap('assets\\logo.ico')


class Converter():
    def __init__(self):
        self.parentValue = StringVar()
        self.parentsList = ['. . .','Length','Weight','Power']
        self.childValue = StringVar()
        self.childrenList = []
        self.classesList = ['. . .',KILO__METER(),METER__KILO(),KILO__MILE(),MILE__KILO(),KILO__GRAM(),GRAM__KILO(),KILO__POUND(),POUND__KILO(),WATT__HP(),HP__WATT(),WATT__JOULEHOUR(),JOULEHOUR__WATT()]
        self.dict = {}
        self.showParents()


    def showParents(self):
        for i in range(0, 5):
            for y in range(0, 2):
                self.frame = Frame(root, borderwidth = 1)
                self.frame.grid(row = 0, column = i, padx = 65)
        self.parentLabel = Label(root, text = 'Choose a category')
        self.parentLabel.grid(row = 0, column = 0, padx = 10, pady = 30, sticky='e')
        self.parentOption = ttk.OptionMenu(root, self.parentValue, self.parentsList[0], *self.parentsList, command = self.changeParent)
        self.parentOption.grid(row = 0, column = 1, padx = 25, pady = 10, sticky='w')


    def changeParent(self, *args):
        coverLayer = Label(root)
        coverLayer.place(width = 350, height = 250, y = 60)
        self.childrenList = []
        for i in range(1, len(self.classesList)):
            if self.parentValue.get() == self.classesList[i].cat:
                self.childrenList.append(self.classesList[i].child)
                self.dict[self.classesList[i].child] = self.classesList[i].multiplier
            elif self.parentValue.get() == '. . .':
                quit()
        self.showChildren()


    def showChildren(self):
        self.childLabel = Label(root, text = 'Choose an option')
        self.childLabel.grid(row = 1, column = 0, padx = 10, pady = 10, sticky='e')
        self.childOption = ttk.OptionMenu(root, self.childValue, self.childrenList[0], *self.childrenList, command = self.changeChild)
        self.childOption.grid(row = 1, column = 1, padx = 25, pady = 10, sticky='w')
        self.entryLabel = Label(root, text = f'{self.childValue.get().split(" > ")[0]}')
        self.entryLabel.grid(row = 2, column = 0, padx = 10, sticky='e')
        self.entry = Entry(root, width = 15)
        self.entry.grid(row = 2, column = 1, padx = 25, pady = 10, sticky='w')
        self.entry.focus()
        self.button = Button(root, text = 'Convert', width = 12, height = 2, command = self.convert)
        self.button.grid(row = 3, column = 1, padx = 25, pady = 10, sticky='w')
        self.outputLabel = Label(root, text = f'{self.childValue.get().split(" > ")[1]}')
        self.outputLabel.grid(row = 4, column = 0, padx = 10, sticky='e')
        self.message = Message(root, text = '0', width = 90)
        self.message.grid(row = 4, column = 1, padx = 25, pady = 10, sticky='w')


    def cleanChild(self):
        self.entry.delete(0, END)
        self.message['text'] = '0'


    def changeChild(self, *args):
        self.cleanChild()
        for i in range(0, len(self.childrenList)):
            if self.childValue.get() == self.childrenList[i]:
                self.entryLabel['text'] = self.childValue.get().split(" > ")[0]
                self.outputLabel['text'] = self.childValue.get().split(" > ")[1]
            else:
                self.cleanChild()


    def convert(self):
            for key in self.dict:
                if key == self.childValue.get():
                    try:
                        result = int(self.entry.get()) * self.dict[key]
                        self.message['text'] = str(round(result, 4))
                    except ValueError:
                        try:
                            result = float(self.entry.get()) * self.dict[key]
                            self.message['text'] = str(round(result, 4))
                        except ValueError:
                            self.cleanChild()


class KILO__METER(Converter):
    def __init__(self):
        self.cat = 'Length'
        self.child = 'Kilometers > Meters'
        self.multiplier = 1000
        
class METER__KILO(Converter):
    def __init__(self):
        self.cat = 'Length'
        self.child = 'Meters > Kilometers'
        self.multiplier = 0.001

class KILO__MILE(Converter):
    def __init__(self):
        self.cat = 'Length'
        self.child = 'Kilometers > Miles'
        self.multiplier = 0.6214
        
class MILE__KILO(Converter):
    def __init__(self):
        self.cat = 'Length'
        self.child = 'Miles > Kilometers'
        self.multiplier = 1.6093

class KILO__GRAM(Converter):
    def __init__(self):
        self.cat = 'Weight'
        self.child = 'Kilograms > Grams'
        self.multiplier = 1000
        
class GRAM__KILO(Converter):
    def __init__(self):
        self.cat = 'Weight'
        self.child = 'Grams > Kilograms'
        self.multiplier = 0.001

class KILO__POUND(Converter):
    def __init__(self):
        self.cat = 'Weight'
        self.child = 'Kilograms > Pounds'
        self.multiplier = 2.205
        
class POUND__KILO(Converter):
    def __init__(self):
        self.cat = 'Weight'
        self.child = 'Pounds > Kilograms'
        self.multiplier = 0.4535

class WATT__HP(Converter):
    def __init__(self):
        self.cat = 'Power'
        self.child = 'Watt > HP'
        self.multiplier = 0.00134
        
class HP__WATT(Converter):
    def __init__(self):
        self.cat = 'Power'
        self.child = 'HP > Watt'
        self.multiplier = 745.7

class WATT__JOULEHOUR(Converter):
    def __init__(self):
        self.cat = 'Power'
        self.child = 'Watt > Joule/Hour'
        self.multiplier = 3600
        
class JOULEHOUR__WATT(Converter):
    def __init__(self):
        self.cat = 'Power'
        self.child = 'Joule/Hour > Watt'
        self.multiplier = 0.000277

if __name__ == '__main__':
    converter = Converter()
    
root.mainloop()
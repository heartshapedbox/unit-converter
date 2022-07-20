from tkinter import *
from tkinter import ttk
from turtle import width
import customtkinter
customtkinter.set_default_color_theme('dark-blue')
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\unit-converter\\')


root = customtkinter.CTk()
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
        self.classesList = ['. . .',KILO__METER(),METER__KILO(),KILO__MILE(),MILE__KILO(),KILO__GRAM(),GRAM__KILO(),KILO__POUND(),POUND__KILO(),WATT__HP(),HP__WATT(),WATT__JOULEHOUR(),JOULEHOUR__WATT()]
        self.dict = {}
        self.showParents()


    def showParents(self):
        for i in range(0, 5):
            for y in range(0, 2):
                self.frame = Frame(root, borderwidth = 1)
                self.frame.grid(row = 0, column = i, padx = 65)
        self.parentLabel = customtkinter.CTkLabel(root, text = 'Choose a category')
        self.parentLabel.grid(row = 0, column = 0, padx = 10, pady = 30, sticky='e')
        self.parentValue.set(self.parentsList[0])
        self.parentOption = customtkinter.CTkComboBox(root, variable=f"{self.parentValue}", values=[*self.parentsList], command = self.changeParent)
        self.parentOption.grid(row = 0, column = 1, padx = 25, pady = 10, sticky='w')

    def changeParent(self, *args):
        coverLayer = customtkinter.CTkLabel(root, text = '')
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
        self.childLabel = customtkinter.CTkLabel(root, text = 'Choose an option')
        self.childLabel.grid(row = 1, column = 0, padx = 10, pady = 10, sticky='e')
        self.childValue.set(self.childrenList[0])
        self.childOption = customtkinter.CTkComboBox(root, variable=f"{self.childValue}", values = [*self.childrenList], command = self.changeChild)
        self.childOption.grid(row = 1, column = 1, padx = 25, pady = 10, sticky='w')
        self.entryLabel = customtkinter.CTkLabel(root, text = f'{self.childValue.get().split(" > ")[0]}')
        self.entryLabel.grid(row = 2, column = 0, padx = 10, sticky='e')
        self.entry = customtkinter.CTkEntry(root, width = 120)
        self.entry.grid(row = 2, column = 1, padx = 25, pady = 10, sticky='w')
        self.entry.focus()
        self.button = customtkinter.CTkButton(root, text = 'Convert', width = 120, height = 35, cursor = 'hand2', command = self.convert)
        self.button.grid(row = 3, column = 1, padx = 25, pady = 10, sticky='w')
        self.outputLabel = customtkinter.CTkLabel(root, text = f'{self.childValue.get().split(" > ")[1]}')
        self.outputLabel.grid(row = 4, column = 0, padx = 10, sticky='e')
        self.message = customtkinter.CTkLabel(root, text = '0', justify = LEFT)
        self.message.grid(row = 4, column = 1, padx = 12, sticky='w')


    def cleanChild(self):
        self.entry.delete(0, END)
        self.message.configure(text = '0')


    def changeChild(self, args):
        self.cleanChild()
        for i in range(0, len(self.childrenList)):
            if self.childValue.get() == self.childrenList[i]:
                self.entryLabel.configure(text = self.childValue.get().split(" > ")[0])
                self.outputLabel.configure(text = self.childValue.get().split(" > ")[1])
            else:
                self.cleanChild()


    def convert(self):
            for key in self.dict:
                if len(self.entry.get()) > 14:
                    self.cleanChild()
                else:
                    if key == self.childValue.get():
                        try:
                            result = int(self.entry.get()) * self.dict[key]
                            self.message.configure(text = str(round(result, 4)))
                        except ValueError:
                            try:
                                result = float(self.entry.get()) * self.dict[key]
                                self.message.configure(text = str(round(result, 4)))
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
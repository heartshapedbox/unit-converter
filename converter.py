from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Unit Converter')
root.geometry('350x350')
root.resizable(False, False)


class Converter():
    def __init__(self):
        self.parentsDict = {}
        self.parentsStrList = ['. . .','Distance: Kilometer > Meter','Distance: Kilometer > Miles','Weight: Kilogram > Gram','Weight: Kilogram > Pound','Power: Watt > HP','Power: Watt > Joule/Hour']
        self.parentsClassList = ['. . .', Distance_KILO_METERS(),Distance_KILO_MILES(),Weight_KILO_GRAM(),Weight_KILO_POUND(),Power_WATT_HP(),Power_WATT_JOULEHOUR()]
        self.childStrList = []
        self.parent = StringVar()
        self.child = StringVar()
        self.x = 0
        self.y = 0


    def showParents(self):
        for i in range(0, 5):
            for y in range(0, 2):
                self.frame = Frame(root, borderwidth = 1)
                self.frame.grid(row = 0, column = i, padx = 65)
        self.parentLabel = Label(root, text = 'Choose a category')
        self.parentLabel.grid(row = 0, column = 0, padx = 10, pady = 30, sticky='e')
        self.parentOption = ttk.OptionMenu(root, self.parent, self.parentsStrList[0], *self.parentsStrList, command = self.changeParents)
        self.parentOption.grid(row = 0, column = 1, padx = 25, pady = 10, sticky='w')


    def changeParents(self, *args):
        coverLayer = Label(root)
        coverLayer.place(width = 350, height = 250, y = 60)
        
        for i in range(0, len(self.parentsStrList)):
            self.parentsDict[i] = self.parentsStrList[i]
        
        for i in range(1, len(self.parentsDict)):
            if self.parent.get() == self.parentsDict[i]:
                self.parentsClassList[i].showChild()
            elif self.parent.get() == '. . .':
                quit()


    def showChild(self):
        self.childLabel = Label(root, text = 'Choose an option')
        self.childLabel.grid(row = 1, column = 0, padx = 10, pady = 10, sticky='e')
        
        self.childOption = ttk.OptionMenu(root, self.child, self.childStrList[0], *self.childStrList, command = self.changeChild)
        self.childOption.grid(row = 1, column = 1, padx = 25, pady = 10, sticky='w')
        
        self.entryLabel = Label(root, text = f'{self.childStrList[0].split(" > ")[0]}')
        self.entryLabel.grid(row = 2, column = 0, padx = 10, sticky='e')
        
        self.entry = Entry(root, width = 15)
        self.entry.grid(row = 2, column = 1, padx = 25, pady = 10, sticky='w')
        self.entry.focus()
        
        self.button = Button(root, text = 'Convert', width = 12, height = 2, command = self.convert)
        self.button.grid(row = 3, column = 1, padx = 25, pady = 10, sticky='w')
        
        self.outputLabel = Label(root, text = f'{self.childStrList[0].split(" > ")[1]}')
        self.outputLabel.grid(row = 4, column = 0, padx = 10, sticky='e')
        
        self.message = Message(root, text = '0', width = 90)
        self.message.grid(row = 4, column = 1, padx = 25, pady = 10, sticky='w')


    def cleanChild(self):
        self.message['text'] = '0'
        self.entry.delete(0, END)


    def changeChild(self, *args):
        self.cleanChild()
        if self.child.get() == self.childStrList[0]:
            self.entryLabel['text'] = self.childStrList[0].split(' > ')[0]
            self.outputLabel['text'] = self.childStrList[0].split(' > ')[1]
        elif self.child.get() == self.childStrList[1]:
            self.entryLabel['text'] = self.childStrList[1].split(' > ')[0]
            self.outputLabel['text'] = self.childStrList[1].split(' > ')[1]
        else:
            self.cleanChild()


    def convert(self):
        if self.child.get() == self.childStrList[0]:
            try:
                result = int(self.entry.get()) * self.x
                self.message['text'] = str(round(result, 4))
            except ValueError:
                try:
                    result = float(self.entry.get()) * self.x
                    self.message['text'] = str(round(result, 4))
                except ValueError:
                    self.cleanChild()           
        else:
            try:
                result = int(self.entry.get()) * self.y
                self.message['text'] = str(round(result, 4))
            except ValueError:
                try:
                    result = float(self.entry.get()) * self.y
                    self.message['text'] = str(round(result, 4))
                except ValueError:
                    self.cleanChild()


class Distance_KILO_METERS(Converter):
    def __init__(self):
        self.childStrList = ['Kilometers > Meters','Meters > Kilometers']
        self.child = StringVar()
        self.x = 1000
        self.y = 0.001


class Distance_KILO_MILES(Converter):
    def __init__(self):
        self.childStrList = ['Kilometers > Miles','Miles > Kilometers']
        self.child = StringVar()
        self.x = 0.6214
        self.y = 1.6093


class Weight_KILO_GRAM(Converter):
    def __init__(self):
        self.childStrList = ['Kilograms > Grams','Grams > Kilograms']
        self.child = StringVar()
        self.x = 1000
        self.y = 0.001


class Weight_KILO_POUND(Converter):
    def __init__(self):
        self.childStrList = ['Kilograms > Pounds','Pounds > Kilograms']
        self.child = StringVar()
        self.x = 2.205
        self.y = 0.4535


class Power_WATT_HP(Converter):
    def __init__(self):
        self.childStrList = ['Watt > HP','HP > Watt']
        self.child = StringVar()
        self.x = 0.00134
        self.y = 745.7


class Power_WATT_JOULEHOUR(Converter):
    def __init__(self):
        self.childStrList = ['Watt > Joule/Hour','Joule/Hour > Watt']
        self.child = StringVar()
        self.x = 3600
        self.y = 0.000277


converter = Converter().showParents()
root.mainloop()
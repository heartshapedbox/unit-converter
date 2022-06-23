from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Converter')
root.geometry('350x350')
root.resizable(False, False)


class Converter():
    def __init__(self):
        self.options = ['','']
        self.parentsList = ['. . .','Distance: Kilometer > Meter','Distance: Kilometer > Miles','Weight: Kilogram > Gram','Weight: Kilogram > Pound']
        self.parent = StringVar()
        self.val = StringVar()
        self.x = 0
        self.y = 0


    def showParents(self):
        for i in range(0, 5):
            for y in range(0, 2):
                self.frame = Frame(root, borderwidth = 1)
                self.frame.grid(row = 0, column = i)
                
        self.parentLabel = Label(root, text = 'Choose a category')
        self.parentLabel.grid(row = 0, column = 0, padx = 10, pady = 30, sticky='e')
        
        self.parentOption = ttk.OptionMenu(root, self.parent, self.parentsList[0], *self.parentsList, command = self.changeParents)
        self.parentOption.grid(row = 0, column = 1, padx = 25, pady = 10, sticky='w')


    def changeParents(self, *args):
        coverLayer = Label(root)
        coverLayer.place(width = 350, height = 250, y = 60)
        
        if self.parent.get() == self.parentsList[1]:
            DistanceKILOMETERS().showChild()
        elif self.parent.get() == self.parentsList[2]:
            DistanceKILOMILES().showChild()
        elif self.parent.get() == self.parentsList[3]:
            WeightKILOGRAM().showChild()
        elif self.parent.get() == self.parentsList[4]:
            WeightKILOPOUND().showChild()
        else:
            quit()
            
                

    def showChild(self):
        self.childLabel = Label(root, text = 'Choose an option')
        self.childLabel.grid(row = 1, column = 0, padx = 10, pady = 10, sticky='e')
        
        self.childOption = ttk.OptionMenu(root, self.val, self.options[0], *self.options, command = self.changeChild)
        self.childOption.grid(row = 1, column = 1, padx = 25, pady = 10, sticky='w')
        
        self.entryLabel = Label(root, text = f'{self.options[0].split(" > ")[0]}')
        self.entryLabel.grid(row = 2, column = 0, padx = 10, sticky='e')
        
        self.entry = Entry(root, width = 15)
        self.entry.grid(row = 2, column = 1, padx = 25, pady = 10, sticky='w')
        self.entry.focus()
        
        self.button = Button(root, text = 'Convert', width = 12, height = 2, command = self.convert)
        self.button.grid(row = 3, column = 1, padx = 25, pady = 10, sticky='w')
        
        self.outputLabel = Label(root, text = f'{self.options[0].split(" > ")[1]}')
        self.outputLabel.grid(row = 4, column = 0, padx = 10, sticky='e')
        
        self.message = Message(root, text = '0', width = 90)
        self.message.grid(row = 4, column = 1, padx = 25, pady = 10, sticky='w')
    
    
    def cleanChild(self):
        self.message['text'] = '0'
        self.entry.delete(0, END)
    
    
    def changeChild(self, *args):
        self.cleanChild()
        if self.val.get() == self.options[0]:
            self.entryLabel['text'] = self.options[0].split(' > ')[0]
            self.outputLabel['text'] = self.options[0].split(' > ')[1]
        elif self.val.get() == self.options[1]:
            self.entryLabel['text'] = self.options[1].split(' > ')[0]
            self.outputLabel['text'] = self.options[1].split(' > ')[1]
        else:
            self.cleanChild()


    def convert(self):
        if self.val.get() == self.options[0]:
            try:
                result = int(self.entry.get()) * self.x
                self.message['text'] = str(round(result, 3))
            except ValueError:
                try:
                    result = float(self.entry.get()) * self.x
                    self.message['text'] = str(round(result, 3))
                except ValueError:
                    self.cleanChild()           
        else:
            try:
                result = int(self.entry.get()) * self.y
                self.message['text'] = str(round(result, 3))
            except ValueError:
                try:
                    result = float(self.entry.get()) * self.y
                    self.message['text'] = str(round(result, 3))
                except ValueError:
                    self.cleanChild()


class DistanceKILOMETERS(Converter):
    def __init__(self):
        self.options = ['Kilometers > Meters','Meters > Kilometers']
        self.val = StringVar()
        self.x = 1000
        self.y = 0.001


class DistanceKILOMILES(Converter):
    def __init__(self):
        self.options = ['Kilometers > Miles','Miles > Kilometers']
        self.val = StringVar()
        self.x = 0.6214
        self.y = 1.6093


class WeightKILOGRAM(Converter):
    def __init__(self):
        self.options = ['Kilograms > Grams','Grams > Kilograms']
        self.val = StringVar()
        self.x = 1000
        self.y = 0.001


class WeightKILOPOUND(Converter):
    def __init__(self):
        self.options = ['Kilograms > Pounds','Pounds > Kilograms']
        self.val = StringVar()
        self.x = 2.205
        self.y = 0.4535


converter = Converter().showParents()
root.mainloop()
from tkinter import *
from threading import Timer
import customtkinter
import pyperclip
import os
os.chdir('C:\\Users\\Dima\\Documents\\GitHub\\unit-converter\\')
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('dark-blue')


class Converter(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Unit Converter')
        self.iconbitmap('assets\\logo.ico')
        x = int(self.winfo_screenwidth() // 2)
        y = int(self.winfo_screenheight() * 0.2)
        x, y = str(x), str(y)
        self.geometry(f'370x380+{x}+{y}')
        self.resizable(False, False)

        self.parent_value = StringVar()
        self.parentsList = ['. . .','Length','Weight','Power']
        self.child_value1 = StringVar()
        self.child_value2 = StringVar()
        self.classes_list = ['. . .',KILO__METER(),METER__KILO(),KILO__MILE(),MILE__KILO(),MILE__METER(),METER__MILE(),KILO__GRAM(),GRAM__KILO(),KILO__POUND(),POUND__KILO(),POUND__GRAM(),GRAM__POUND(),WATT__HP(),HP__WATT(),WATT__JOULEHOUR(),JOULEHOUR__WATT(),JOULEHOUR__HP(),HP__JOULEHOUR()]
        self.dict = {}
        
        self.accent_color1 = '#363336'
        self.accent_color2 = '#2e4f87'
        self.accent_color3 = '#608bd5'
        self.accent_color4 = '#f757a4'
        self.accent_color5 = '#d6478d'
        
        self.show_parents()


    def show_parents(self):
        self.parent_label = customtkinter.CTkLabel(self, text = 'Category')
        self.parent_label.grid(row = 0, column = 0, padx = 50, pady = 20, sticky='w')
        self.parent_value.set(self.parentsList[0])
        self.parent_option = customtkinter.CTkOptionMenu(self, variable=self.parent_value, values=[*self.parentsList], command = self.change_parent)
        self.parent_option.grid(row = 0, column = 1, pady = 10, sticky='w')
        self.parent_option.configure(width = 160, button_color = self.accent_color1, button_hover_color = self.accent_color1, dropdown_hover_color = self.accent_color2)
        self.parent_option.focus()


    def change_parent(self, *args):
        self.cover_layer = customtkinter.CTkLabel(self, text = '')
        self.cover_layer.place(width = 350, height = 500, y = 70)
        self.children_list, self.children_list1, self.children_list2 = [], [], []
        
        for i in range(1, len(self.classes_list)):
            if self.parent_value.get() == self.classes_list[i].cat:
                self.children_list.append(self.classes_list[i].child)
                self.dict[self.classes_list[i].child] = self.classes_list[i].multiplier
                
                if self.classes_list[i].child.split(' > ')[0] not in self.children_list1:
                    self.children_list1.append(self.classes_list[i].child.split(' > ')[0])
                if self.classes_list[i].child.split(' > ')[1] not in self.children_list2:
                    self.children_list2.append(self.classes_list[i].child.split(' > ')[1])
                    
            elif self.parent_value.get() == '. . .':
                quit()
        self.show_children()


    def show_children(self):
        self.child_label1 = customtkinter.CTkLabel(self, text = 'From')
        self.child_label1.grid(row = 1, column = 0, padx = 50, pady = 10, sticky='w')
        self.child_value1.set(self.children_list[0].split(' > ')[0])
        self.child_option1 = customtkinter.CTkOptionMenu(self, variable=self.child_value1, values = [*self.children_list1], command = self.change_child)
        self.child_option1.grid(row = 1, column = 1, pady = 10, sticky='w')
        self.child_option1.configure(width = 160, button_color = self.accent_color1, button_hover_color = self.accent_color1, dropdown_hover_color = self.accent_color2)
        
        self.child_label2 = customtkinter.CTkLabel(self, text = 'To')
        self.child_label2.grid(row = 2, column = 0, padx = 50, pady = 10, sticky='w')
        self.child_value2.set(self.children_list[0].split(' > ')[1])
        self.child_option2 = customtkinter.CTkOptionMenu(self, variable=self.child_value2, values = [*self.children_list2], command = self.change_child)
        self.child_option2.grid(row = 2, column = 1, pady = 10, sticky='w')
        self.child_option2.configure(width = 160, button_color = self.accent_color1, button_hover_color = self.accent_color1, dropdown_hover_color = self.accent_color2)
        
        self.entry_label = customtkinter.CTkLabel(self, text = f'{self.child_value1.get()}', text_color = self.accent_color3)
        self.entry_label.grid(row = 3, column = 0, padx = 50, sticky='w')
        self.entry = customtkinter.CTkEntry(self, width = 160)
        self.entry.grid(row = 3, column = 1, pady = 10, sticky='w')
        self.entry.focus()
        self.convert_button = customtkinter.CTkButton(self, text = 'Convert', width = 160, height = 35, cursor = 'hand2', command = self.convert)
        self.convert_button.grid(row = 4, column = 1, pady = 10, sticky='w')
        self.convert_button.configure(hover_color = self.accent_color2)
        self.switch_val = customtkinter.StringVar(value = "on")
        self.switch = customtkinter.CTkSwitch(self, text = '', cursor = 'hand2', variable = self.switch_val, onvalue = "on", offvalue = "off", command = self.switch_child)
        self.switch.grid(row = 4, column = 0, pady = 20, sticky='e')
        self.switch.configure(fg_color = self.accent_color2)
        self.output_label = customtkinter.CTkLabel(self, text = f'{self.child_value2.get()}', text_color = self.accent_color3)
        self.output_label.grid(row = 5, column = 0, padx = 50, sticky='w')
        self.output = customtkinter.CTkLabel(self, text = '0', justify = LEFT)
        self.output.grid(row = 5, column = 1, sticky='w')
        self.copy_button = customtkinter.CTkButton(self, text = 'Copy', width = 70, height = 35, cursor = 'hand2', command = self.copy)
        self.copy_button.grid(row = 6, column = 1, pady = 20, sticky='e')
        self.copy_button.configure(hover_color = self.accent_color2)
        self.reset_button = customtkinter.CTkButton(self, text = 'Reset', width = 70, height = 35, cursor = 'hand2', command = self.reset)
        self.reset_button.grid(row = 6, column = 0, pady = 20, sticky='s')
        self.reset_button.configure(fg_color = self.accent_color4, hover_color = self.accent_color5)
        self.copy_message = customtkinter.CTkLabel(self, text = '', width = 1, justify = RIGHT)
        self.copy_message.grid(row = 6, column = 1, padx = 20, pady = 20, sticky='w')
        self.copy_message.configure(text_color = self.accent_color3)
    

    def clean_child(self):
        self.entry.delete(0, END)
        self.output.configure(text = '0')


    def change_child(self, args):
        self.entry.configure(state = 'normal')
        self.entry.focus()
        self.copy_message.configure(text = '')
        self.clean_child()
        for i in range(0, len(self.children_list1)):
            if self.children_list1[i] != self.children_list2[i]:
                self.entry_label.configure(text = self.child_value1.get())
                self.output_label.configure(text = self.child_value2.get())
            elif self.child_value1.get() == self.child_value2.get():
                self.entry.configure(state = 'disable')
    
    
    def switch_child(self):
        self.entry_label.configure(text = self.child_value2.get())
        self.output_label.configure(text = self.child_value1.get())
        i = self.child_option2.get()
        y = self.child_option1.get()
        self.child_option1.set(i)
        self.child_option2.set(y)
        
    

    def convert(self):
        self.clip = ''
        for key in self.dict:
            if len(self.entry.get()) > 20:
                self.clean_child()
            else:
                self.child_value = f'{self.child_value1.get()} > {self.child_value2.get()}'
                if key == self.child_value:
                    try:
                        self.result = int(self.entry.get()) * self.dict[key]
                        self.output.configure(text = str(round(self.result, 10)))
                        self.clip = str(round(self.result, 10))
                    except ValueError:
                        try:
                            self.result = float(self.entry.get()) * self.dict[key]
                            self.output.configure(text = str(round(self.result, 10)))
                            self.clip = str(round(self.result, 10))
                        except ValueError:
                            self.clean_child()
                     
    
    def reset(self):
        for i in (self.child_label1, self.child_label2, self.child_option1, self.child_option2, self.entry_label, self.entry, self.convert_button, self.output_label, self.output, self.copy_button, self.reset_button, self.copy_message, self.switch):
            i.destroy()
        converter = Converter()
    
    
    def reset_copy_message(self):
        self.copy_message.configure(text = '')
    
    
    def copy(self):
        pyperclip.copy(self.clip)
        self.copy_message.configure(text = 'Copied!')
        Timer(0.5, self.reset_copy_message).start()
   




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

class MILE__METER(Converter):
    def __init__(self):
        self.cat = 'Length'
        self.child = 'Miles > Meters'
        self.multiplier = 1609

class METER__MILE(Converter):
    def __init__(self):
        self.cat = 'Length'
        self.child = 'Meters > Miles'
        self.multiplier = 0.0006214
        
        


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

class POUND__GRAM(Converter):
    def __init__(self):
        self.cat = 'Weight'
        self.child = 'Pounds > Grams'
        self.multiplier = 453.5
        
class GRAM__POUND(Converter):
    def __init__(self):
        self.cat = 'Weight'
        self.child = 'Grams > Pounds'
        self.multiplier = 0.002205




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

class JOULEHOUR__HP(Converter):
    def __init__(self):
        self.cat = 'Power'
        self.child = 'Joule/Hour > HP'
        self.multiplier = 0.00000037

class HP__JOULEHOUR(Converter):
    def __init__(self):
        self.cat = 'Power'
        self.child = 'HP > Joule/Hour'
        self.multiplier = 2684519.53

if __name__ == '__main__':
    Converter().mainloop()
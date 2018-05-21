import tkinter
import custom
from tkinter import filedialog
import pickle

class Application:
    def __init__(self):
        self.__inventory = []
        self.__selected_index = -1
        self.__selected_inventory = None

        self.__window = tkinter.Tk()
        self.__window.title('inventory') 
        
        self.__first = tkinter.StringVar()
        self.__second = tkinter.StringVar()
        self.__third = tkinter.StringVar()
        self.__forth = tkinter.StringVar()
        
        self.build_input_frame('brand name: ', self.__first)
        self.build_input_frame('product name: ', self.__second)
        self.build_input_frame('SKU: ', self.__third)
        self.build_input_frame('price: ', self.__forth)

        frame = tkinter.Frame(self.__window)
        self.__add_button = tkinter.Button(frame, text='Add inventory', anchor=tkinter.W, command=self.add_inventory)
        self.__add_button.pack(side='left')
        self.__save_button = tkinter.Button(frame, text='Save inventory', anchor=tkinter.W, command=self.save_inventory, state=tkinter.DISABLED)
        self.__save_button.pack(side='left')
        self.__delete_button = tkinter.Button(frame, text='Delete inventory', anchor=tkinter.W, command=self.delete_inventory, state=tkinter.DISABLED)
        self.__delete_button.pack()
        frame.pack()

        frame = tkinter.Frame(self.__window)
        label = tkinter.Label(frame, text='Your inventory')
        self.__inventory_list = tkinter.Listbox(frame, width=120, selectmode=tkinter.SINGLE)
        self.__inventory_list.bind('<<ListboxSelect>>', self.select_inventory)
        label.pack()
        self.__inventory_list.pack()
        frame.pack()

        frame = tkinter.Frame(self.__window)
        label = tkinter.Label(frame, text='save or open a file?')
        self.__save_file_button = tkinter.Button(frame, text='save a file', command=self.save_file)
        self.__save_file_button.pack()
        self.__open_file_button = tkinter.Button(frame, text='open a file', command=self.open_file)
        self.__open_file_button.pack()
        frame.pack()

    def save_file(self):
        filename=filedialog.asksaveasfilename()
        f = open(filename, 'wb')
        pickle.dump(self.__inventory, f)
        f.close()

    def open_file(self):
        filename=filedialog.askopenfilename()
        f = open(filename, 'rb') 
        x = pickle.load(f)
        self.__inventory += x
        for i in x:
            self.__inventory_list.insert(tkinter.END,str(i))
        f.close()
    
    def build_input_frame(self, label, textvariable):
        frame = tkinter.Frame(self.__window)
        label = tkinter.Label(frame, text=label, width=15, anchor=tkinter.W)
        entry = tkinter.Entry(frame, textvariable=textvariable, width=30)
        label.pack(side='left')
        entry.pack(side='right')
        frame.pack()

    def add_inventory(self):
        """Get the values from the bound variables and create a new Contact."""
        c = custom.Custom(self.__first.get(), self.__second.get(), self.__third.get(), self.__forth.get())
        self.__inventory.append(c)

        self.__inventory_list.insert(tkinter.END, str(c))

    def select_inventory(self, event):
        """Get the Contact at the index selected, and set the Entry fields
           with its values."""
        # Get the current selection from the Listbox. curselection() returns
        # a tuple and we want the first item
        # Get the current selection from the Listbox. curselection() returns
        # a tuple and we want the first item
        current_selection = self.__inventory_list.curselection()
        if current_selection:
            self.__selected_index = current_selection[0]


            # Grab the Contact object from self.__contacts at that index
            self.__selected_inventory = self.__inventory[self.__selected_index]


            # Use it's values to set the StringVars
            self.__first.set(self.__selected_inventory.get_first())
            self.__second.set(self.__selected_inventory.get_second())
            self.__third.set(self.__selected_inventory.get_third())
            self.__forth.set(self.__selected_inventory.get_forth())


            # Make sure the Save button is enabled
            self.__save_button.config(state=tkinter.NORMAL)
            self.__delete_button.config(state=tkinter.NORMAL)


    def delete_inventory(self):
        """Remov the Contact at the index selected then set the Entry fields
           to empty values."""
        if 0 <= self.__selected_index < len(self.__inventory):
            del self.__inventory[self.__selected_index]
            self.__inventory_list.delete(self.__selected_index)


            # Call the method to deselect the item, clear Entry fields, and
            # disable buttons.
            self.after_selected_operation()


    def save_inventory(self):
        """Set the selected Contact's fields and then persist its __str__
           representation to the Listbox."""
        self.__selected_inventory.set_first(self.__first.get())
        self.__selected_inventory.set_second(self.__second.get())
        self.__selected_inventory.set_third(self.__third.get())
        self.__selected_inventory.set_forth(self.__forth.get())


        # Listbox widgets don't have a way of updating an item in place. So
        # We'll delete the item at a particular index and then add it
        self.__inventory_list.delete(self.__selected_index)
        self.__inventory_list.insert(self.__selected_index, str(self.__selected_inventory))


        # Call the method to deselect the item, clear Entry fields, and
        # disable buttons.
        self.after_selected_operation()




    def after_selected_operation(self):
        """Clear the selected index, contact, and disable buttons."""
        self.__selected_index = -1
        self.__selected_inventory = None


        self.__first.set('')
        self.__second.set('')
        self.__third.set('')
        self.__forth.set('')


        # Make sure the Save and Delete buttons are disabled
        self.__save_button.config(state=tkinter.DISABLED)
        self.__delete_button.config(state=tkinter.DISABLED)




    def start(self):
        tkinter.mainloop()
        

        
def main():
    app = Application()
    app.start()
    
main() 

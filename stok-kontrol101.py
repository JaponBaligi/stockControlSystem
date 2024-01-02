from tkinter import *

root = Tk()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, search_val):
        current = self.head
        while current:
            if current.data[0] == search_val:
                return current.data
            current = current.next
        return None

    def delete(self, delete_val):
        current = self.head
        if current and current.data[0] == delete_val:
            self.head = current.next
            return
        prev = None
        while current and current.data[0] != delete_val:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

class StokKontrol(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('Stok Kontrol Sistemi')
        self.grid()
        self.items_list = LinkedList()
        root.geometry("650x450")
        self.itemCount = 0

        Label(self, text='Arama Yap (Item Numarasına Göre): ').grid(row=0,
                                                        column=1, padx=6, pady=20, sticky=E)

        self._box1 = IntVar()
        self._input = Entry(self, width=20, textvariable=self._box1)
        self._input.grid(row=0, column=2, padx=8, pady=20, sticky=W)

        self.btn1 = Button(self, text='Ara',
                           command=self.searchInventory)
        self.btn1.grid(row=0, column=3, padx=8, pady=20, sticky=W)

        self.btn2 = Button(self, text='Yenile', command=self.resetList)
        self.btn2.grid(row=0, column=4, padx=8, pady=20, sticky=W)

        self.scroll = Scrollbar(self)
        self.scroll.grid(row=3, column=4)
        self.text = Text(self, width=60, height=10, wrap=WORD,
                         yscrollcommand=self.scroll.set)
        self.text.grid(row=3, column=0, columnspan=5, padx=20, pady=20)
        self.scroll.config(command=self.text.yview)

        Label(self, text="Item Bilgileri:").grid(row=4, column=0, pady=5, sticky=N)

        Label(self, text='Item Numarası ').grid(row=6, column=0, padx=6,
                                              pady=6, sticky=W)

        self._box2 = StringVar()
        self._input1 = Entry(self, width=40, textvariable=self._box2)
        self._input1.grid(row=6, column=1, padx=8, pady=10, sticky=E)

        Label(self, text='Item Adı ').grid(row=6, column=2, padx=6,
                                            pady=6, sticky=E)

        self._box3 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box3)
        self._input.grid(row=6, column=3, padx=8, pady=10, sticky=E)

        Label(self, text='Mevcut ').grid(row=10, column=0, padx=6,
                                          pady=6, sticky=E)

        self._box4 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box4)
        self._input.grid(row=10, column=1, padx=8, pady=10, sticky=W)

        Label(self, text='Fiyat ').grid(row=10, column=2, padx=6,
                                        pady=6, sticky=E)

        self._box5 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box5)
        self._input.grid(row=10, column=3, padx=8, pady=10)

        self.btn3 = Button(self, text='Item Ekle', command=self.addItem)
        self.btn3.grid(row=11, column=1, padx=5, pady=20, sticky=W)

        self.btn4 = Button(self, text='Itemi Düzenle',
                           command=self.editItem)
        self.btn4.grid(row=11, column=2, padx=5, pady=20, sticky=W)

        self.btn5 = Button(self, text='Itemi Sil',
                           command=self.deleteItem)
        self.btn5.grid(row=11, column=3, padx=5, pady=20, sticky=W)

        self.text.insert(END, 'Item Numarası' + '\t\t' + 'Item Adı'
                         + '\t\t' + 'Adet' + '\t\t' + 'Fiyat'
                         + '\t\t')
        self.text.insert(END,
                         '------------------------------------------------------------'
                         )
        self.text.configure(state="disabled")
        self._input1.focus_set()

    def resetList(self):
        self.text.configure(state="normal")
        self.text.delete(1.0, END)
        self.text.insert(END, 'Item Numarası' + '\t\t' + 'Item Adı'
                         + '\t\t' + 'Mevcut' + '\t\t' + 'Tutar'
                         + '\t\t')
        self.text.insert(END,
                         '------------------------------------------------------------'
                         )

        current = self.items_list.head
        while current:
            self.text.insert(END, current.data[0] + '\t\t' + current.data[1] + '\t\t'
                             + current.data[2] + '\t\t' + current.data[3] + '\t\t')
            current = current.next

        self.text.configure(state="disabled")


    def addItem(self):
        self.text.configure(state="normal")
        self.text.delete(1.0, END)
        self.text.insert(END, 'Item Numarası' + '\t\t' + 'Item Adı'
                         + '\t\t' + 'Mevcut' + '\t\t' + 'Tutar'
                         + '\t\t')
        self.text.insert(END,
                         '------------------------------------------------------------'
                         )

        iNum = self._box2.get()
        iName = self._box3.get()
        oHand = self._box4.get()
        iPrice = self._box5.get()

        if (iNum != '' and iName != '' and oHand != '' and iPrice != ''):
            record = (iNum, iName, oHand, iPrice)
            self.items_list.append(record)

            current = self.items_list.head
            while current:
                self.text.insert(END, current.data[0] + '\t\t' + current.data[1] + '\t\t'
                                 + current.data[2] + '\t\t' + current.data[3] + '\t\t')
                current = current.next
        else:
            self.text.delete(1.0, END)
            self.text.insert(END, 'HATA: Bir ya da daha fazla alan boş bırakıldı.')

        self._box2.set('')
        self._box3.set('')
        self._box4.set('')
        self._box5.set('')
        self._input1.focus_set()

        self.text.configure(state="disabled")

    def searchInventory(self):
        self.text.configure(state="normal")
        self.text.delete(1.0, END)
        self.text.insert(END, 'Item Numarası' + '\t\t' + 'Item Adı'
                         + '\t\t' + 'Mevcut' + '\t\t' + 'Tutar'
                         + '\t\t')
        self.text.insert(END,
                         '------------------------------------------------------------'
                         )

        searchVal = str(self._box1.get())
        result = self.items_list.search(searchVal)

        if result:
            self.text.insert(END, result[0] + '\t\t' + result[1]
                             + '\t\t' + result[2] + '\t\t' + result[3]
                             + '\t\t')
        else:
            self.text.insert(END, 'Item bulunamadı.')

        self.text.configure(state="disabled")

    def clearSearch(self):
        self._box1.set('')

    def editItem(self):
        self.text.configure(state="normal")

        searchVal = str(self._box1.get())

        current = self.items_list.head
        while current:
            if current.data[0] == searchVal:
                iNum = self._box2.get()
                iName = self._box3.get()
                oHand = self._box4.get()
                iPrice = self._box5.get()

                if iNum != '' and iName != '' and oHand != '' and iPrice != '':
                    new_item = (iNum, iName, oHand, iPrice)
                    current.data = new_item

                    self.text.delete(1.0, END)
                    self.text.insert(END, 'Item Numarası' + '\t\t' + 'Item Adı'
                                     + '\t\t' + 'Mevcut' + '\t\t' + 'Fiyat'
                                     + '\t\t')
                    self.text.insert(END,
                                     '------------------------------------------------------------'
                                     )

                    current = self.items_list.head
                    while current:
                        self.text.insert(END, current.data[0] + '\t\t' + current.data[1] + '\t\t'
                                         + current.data[2] + '\t\t' + current.data[3] + '\t\t')
                        current = current.next
                else:
                    self.text.delete(1.0, END)
                    self.text.insert(END, 'HATA: Bir ya da daha fazla alan boş bırakıldı.')

                break

            current = current.next

        self._box1.set('')
        self._box2.set('')
        self._box3.set('')
        self._box4.set('')
        self._box5.set('')
        self._input1.focus_set()

        self.text.configure(state="disabled")

    def deleteItem(self):
        self.text.configure(state="normal")

        searchVal = str(self._box1.get())

        current = self.items_list.head
        prev = None

        while current:
            if current.data[0] == searchVal:
                if prev is None:
                    self.items_list.head = current.next
                else:
                    prev.next = current.next

                self.text.delete(1.0, END)
                self.text.insert(END, 'Item Numarası' + '\t\t' + 'Item Adı'
                                 + '\t\t' + 'Mevcut' + '\t\t' + 'Fiyat'
                                 + '\t\t')
                self.text.insert(END,
                                 '------------------------------------------------------------'
                                 )

                current = self.items_list.head
                while current:
                    self.text.insert(END, current.data[0] + '\t\t' + current.data[1] + '\t\t'
                                     + current.data[2] + '\t\t' + current.data[3] + '\t\t')
                    current = current.next

                break

            prev = current
            current = current.next

        else:
            self.text.delete(1.0, END)
            self.text.insert(END, 'Item bulunamadı.')

        self._box1.set('')
        self.text.configure(state="disabled")

def main():
    StokKontrol().mainloop()

main()

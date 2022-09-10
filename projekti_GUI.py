from tkinter import *
from tkinter.ttk import Combobox
# import os
import csv


root = Tk()

root.title('TimeTable')
# root.iconbitmap('E.ico')
root.geometry('800x500')
root.configure(bg='#B8B8B8')

filePath = Label(root, text='Enter data path:')
filePath.grid(row=0, column=0, padx=0, pady=15, columnspan=2)
filePath.configure(font=('Times', 12, 'bold'), borderwidth=2, relief='flat', bg='white')

path_entry = Entry(root, width=40, borderwidth=5, )
path_entry.grid(row=0, column=2, padx=7, pady=15, columnspan=3)


def display_():
    warnings.delete(0, END)
    # courses.delete(0, END)
    selected_year = year_b.get()
    selected_department = dep_entry.get()
    path = path_entry.get()
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            number = line[0][4]
            number1 = line[0][3]
            # str_year = str(selected_year)
            # str_dep = str(selected_department)
            if selected_year == number and number1 == ' ' or selected_year == number1 and line[0][2] == ' ' or selected_year == line[0][5] and line[0][4] == ' ':
                if selected_department.upper() == line[0][:2] or selected_department.upper() == line[0][:3] or selected_department.upper() == line[0][:4]:
                    courses.insert(END, line)
    dep1 = dep_entry.get()
    list1 = ['UNI', 'CHI', 'CS', 'ECE', 'ECON', 'EE', 'EECS', 'FRE', 'ENGR', 'LIFE', 'ISE', 'IE', 'MGT', 'MATH', 'GER']
    if dep1.upper() in list1:
        # warnings.delete(0, END)
        # warnings.insert(0, ' ')
        return True
    else:
        warnings.delete(0, END)
        warnings.insert(0, '>>>Error: Please check the Department entry!')
    year1 = year_b.current()
    list2 = [1, 2, 3, 4, 5]
    if year1 in list2:
        # warnings.delete(0, END)
        warnings.insert(0, 'No errors in the year selection')
    else:
        warnings.delete(0, END)
        warnings.insert(0, '>>>Error: Please check the Year selection!')

# I kom shkru dy kode per clear function ,
# i pari qe eshte i komentuar eshte per me i fshi vetem selected rows ne courses listbox,
# por po jep error dhe nuk kom mujt me gjete zgjidhjen
# kurse kodi i dyte me rradhe eshte per me i fshi all rows


""" def clear_():
    warnings.delete(0, END)
    a = []
    for i in courses.curselection():
        selected = courses.get(i)
        a.append(selected)
    courses.delete(0, END)
    for i in a():
        courses.insert(i)
    courses.insert(a)
    # for i in courses.curselection():
          selected = courses.get(i)
          courses.delete(selected)
          """


def clear_():
    warnings.delete(0, END)
    courses.delete(0, END)


# mundeni me ndrru path-in se ku doni me rujt csv.file-in me orarin e krijuar
def save_():
    # selected = courses.curselection()
    f = open("C:\\Users\\imfla\\Desktop\\ERISA\\Projekti-GUI\\timetable.csv", "w")
    writer = csv.writer(f)
    for i in courses.curselection():
        selected = courses.get(i)
        writer.writerow(selected)
    f.close()


year = Label(root, text='Year: ')
year.grid(row=1, column=1, padx=0, pady=40, columnspan=1)
year.configure(font=('Times', 10, 'bold'), borderwidth=2, relief='flat', bg='white')

year_b = Combobox(root, width=10, )
year_b['values'] = ('1', '2', '3', '4', '5')
year_b.grid(column=2, row=1, padx=0, pady=40, )
year_b.current()
year_sel = year_b.get()


warnings_L = Label(root, text='Warnings:')
warnings_L.grid(row=4, column=0, pady=35)
warnings_L.configure(font=('Helvetica', 10, 'italic'), borderwidth=2, relief='flat', bg='#FF9999')

courses_L = Label(root, text='Courses:')
courses_L.grid(row=4, column=5, padx=0, pady=40)
courses_L.configure(font=('Helvetica', 10), borderwidth=2, relief='flat', bg='white')

warnings = Listbox(root, width=55, borderwidth=5,)
warnings.grid(row=5, column=0, columnspan=5, padx=5, sticky=W)
courses = Listbox(root, width=55, borderwidth=5, selectmode=MULTIPLE)
scroll = Scrollbar(root, command=courses.yview, borderwidth=5, relief='raised')
scroll1 = Scrollbar(root, orient=HORIZONTAL, borderwidth=5, relief='raised')
scroll1.config(command=courses.xview)
scroll.grid(column=10, row=5,)
scroll1.grid(row=9, column=8)
courses.grid(row=5, column=5, columnspan=5, padx=5, sticky=W)
courses.configure(yscrollcommand=scroll.set, xscrollcommand=scroll1.set)

department = Label(root, text='Department:', width=10)

department.grid(row=1, column=5, padx=0, pady=40)
department.configure(bg='white')

dep_entry = Entry(root, width=30, borderwidth=5)
dep_entry.grid(row=1, column=6, padx=0, pady=40)

display = Button(root, text='Display', width=8, command=display_)
clear = Button(root, text='Clear', width=7, command=clear_)
save = Button(root, text='Save', width=7, command=save_)

display.grid(row=3, column=0, padx=5)
display.configure(borderwidth=5, relief='raised')
clear.grid(row=3, column=1, padx=0)
clear.configure(borderwidth=5, relief='raised')
save.grid(row=3, column=2, padx=0)
save.configure(borderwidth=5, relief='raised')


# C:\Users\imfla\Desktop\ERISA\Projekti-GUI\sampledata.csv
# C:\\Users\\imfla\\Desktop\\ERISA\\Projekti-GUI\\timetable.csv

root.mainloop()

# Ketu perfudon kodi!

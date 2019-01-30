import sqlite3
from tkinter import *
from tkinter import messagebox
from pandas import *
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib
import collections, numpy
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn import tree
import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score


class window:
    def __init__(self, master):
        self.master = master
        self.uname=StringVar()
        self.passw3=StringVar()
        self.sie=IntVar()
        self.apt=IntVar()
        self.gd=IntVar()
        self.pi=IntVar()
        self.pre=StringVar()



        canvas2 = Canvas(self.master, width=150, height=150,  bg="#17202a")

        canvas2.place(x=20, y=75)
        self.master.my_image = PhotoImage(file='logo.png')
        canvas2.create_image(0, 0, anchor="nw", image=self.master.my_image)




        self.ptilte = Label(self.master, text="             ADMIN LOGIN           ", bg="#DBE7FF",
                            font=('Imprint MT Shadow', 13, "bold"),
                            fg="#000055", relief="groove")
        Label(self.master, text="Department Of Computer Science & Engineering", font=('Imprint MT Shadow ', 16, "bold"),
              fg="#fdfefe", bg="#17202a").place(x=70, y=30)
        self.ptilte.pack()
        la1 = Label(self.master, text="NAME:", fg="#fdfefe", font=("", 14, "bold"), bg="#17202a")

        e1 = Entry(self.master, textvariable=self.uname, fg="#000055", font=("", 11, "bold"), relief="sunken", bd=5,
                   bg="#F4FCE3")

        lb1 = Label(self.master, text="USN: ", fg="#fdfefe", font=("", 14, "bold"), bg="#17202a")

        e2 = Entry(self.master, textvariable=self.passw3, fg="#000055", font=("", 11, "bold"),
                   relief="sunken", bd=5, bg="#F4FCE3")
        b1 = Button(self.master, text="LOGIN", command=self.login1, font=("ARIAL", 11, "bold"), bg="#555555",
                    fg="white",
                    relief="raised", bd=5)

        btn = Button(self.master, text="CLOSE", command=self.close, font=("ARIAL", 11, "bold"), bg="#555555",
                    fg="white",
                    relief="raised", bd=5)

        la1.place(x=190, y=100)
        e1.place(x=280, y=100)

        lb1.place(x=205, y=160)
        e2.place(x=280, y=160)

        b1.place(x=250, y=210)
        btn.place(x=400,y=210)



        self.second = Toplevel()
        self.second.geometry("1000x500")
        self.second.configure(background="#17202a")
        self.second.withdraw()

        canvas = Canvas(self.second, width=150, height=150, border=0.5, bg="#17202a", relief="groove", bd=5)
        canvas.configure(border=0.5)
        canvas.place(x=20, y=75)
        self.second.my_image = PhotoImage(file='logo.png')
        canvas.create_image(0, 0, anchor="nw", image=self.master.my_image)

        self.ptilte = Label(self.second, text="             PLACEMENT INFORMATION           ", bg="#DBE7FF",
                            font=('Imprint MT Shadow', 13, "bold"),
                            fg="#000055", relief="groove")
        Label(self.second, text="Department Of Computer Science & Engineering", font=('Imprint MT Shadow ', 16, "bold"),
              fg="#fdfefe", bg="#17202a").place(x=190, y=30)
        self.ptilte.pack()


        l2 = Label(self.second, text="NAME:", fg="#fdfefe", font=("Bookman Old Style", 13, "bold","underline"), bg="#17202a")
        e2 = Entry(self.second, textvariable=self.uname, fg="red", font=("", 11, "bold"), relief="sunken", bd=5,
                   bg="#F4FCE3", justify="center")
        l2.place(x=220, y=140)
        e2.place(x=320, y=140)


        l3 = Label(self.second, text="USN:", fg="#fdfefe", font=("Bookman Old Style", 13, "bold","underline"), bg="#17202a")
        e3 = Entry(self.second, textvariable=self.passw3, fg="red", font=("", 11, "bold"), relief="sunken", bd=5,
                   bg="#F4FCE3", justify="center")
        l3.place(x=560, y=140)
        e3.place(x=650, y=141)


        l4 = Label(self.second, text="SIE:", fg="#fdfefe", font=("Bookman Old Style", 13, "bold","underline"), bg="#17202a")
        e4 = Entry(self.second, textvariable=self.sie, fg="red", font=("", 11, "bold"), relief="sunken", bd=5,
                   bg="#F4FCE3", justify="center")
        l4.place(x=220, y=200)
        e4.place(x=320, y=201)


        l5 = Label(self.second, text="APT:", fg="#fdfefe", font=("Bookman Old Style", 13, "bold","underline"), bg="#17202a")
        e5 = Entry(self.second, textvariable=self.apt, fg="red", font=("", 11, "bold"), relief="sunken", bd=5,
                   bg="#F4FCE3", justify="center")

        l5.place(x=560, y=200)
        e5.place(x=650, y=201)

        l6 = Label(self.second, text="GD:", fg="#fdfefe", font=("Bookman Old Style", 13, "bold","underline"), bg="#17202a")
        e6 = Entry(self.second, textvariable=self.gd, fg="red", font=("", 11, "bold"), relief="sunken", bd=5,
                   bg="#F4FCE3", justify="center")
        l6.place(x=220, y=260)
        e6.place(x=320, y=261)

        l7 = Label(self.second, text="PI:", fg="#fdfefe", font=("Bookman Old Style", 13, "bold","underline"), bg="#17202a")
        e7 = Entry(self.second, textvariable=self.pi, fg="red", font=("", 11, "bold"), relief="sunken", bd=5,
                   bg="#F4FCE3", justify="center")
        l7.place(x=560,y=260)
        e7.place(x=650,y=261)


        bt = Button(self.second, text="Predict", command=self.predict, font=("Bookman Old Style", 11, "bold"), bg="#555555",
                    fg="white",
                    relief="raised", bd=5)
        bt.place(x=450, y=350)

        bt1 = Button(self.second, text="Back", command=self.back, font=("Bookman Old Style", 11, "bold"),
                    bg="#555555",
                    fg="white",
                    relief="raised", bd=5)
        bt1.place(x=600, y=350)



    def clear(self):
        self.uname.set('')
        self.passw3.set('')

    def close(self):
        self.master.destroy()
    def back(self):
        self.clear()
        self.second.withdraw()
        self.master.deiconify()
    def predict(self):
        data = pd.read_csv("placement_data.csv", sep=",")
        y = data.target
        x = data.drop('target', axis=1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.7, random_state=2)

        model = tree.DecisionTreeClassifier(max_depth=5, max_leaf_nodes=10, criterion='entropy')
        model.fit(x_train, y_train)
        y_predict = model.predict([[self.sie.get(), self.apt.get(), self.gd.get(), self.pi.get()]])
        for i in y_predict:
            self.pre.set(i)

        messagebox.showinfo("Placement","Elegible: "+self.pre.get().upper(),icon="info")


    def login1(self):
        self.db = sqlite3.connect('admin1.db')
        self.cnn = self.db.cursor()
        self.sql = "SELECT * FROM STUDENT WHERE NAME=? AND USN=?"
        self.cnn.execute(self.sql,[(self.uname.get()),(self.passw3.get())])
        self.row = self.cnn.fetchone()
        if self.row:
            messagebox.showinfo("WELOCME\n", "Student found")
            self.cer = "SELECT * FROM MARKS WHERE USN=?"
            self.cnn.execute(self.cer, [self.passw3.get()])
            self.row1 = self.cnn.fetchone()
            if self.row1:
                self.sie.set(self.row1[1])
                self.apt.set(self.row1[2])
                self.gd.set(self.row1[3])
                self.pi.set(self.row1[4])




                self.master.withdraw()
                self.second.deiconify()

            else:
                messagebox.showerror("ERROR", "Record Not Found\n Or\n Please Input Correct Student Name And USN")
                self.clear()



        else:
            messagebox.showerror("ERROR", "Record Not Found\n Or\n Please Input Correct Student Name And USN")
            self.clear()










mw = Tk()
mw.geometry("700x400")
mw.configure(background="#17202a",border=0.5)
mw.title("COMPUTER SCIENCE DEPARTMENT")
myapp = window(mw)
mw.mainloop()
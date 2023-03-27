#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from PIL import Image, ImageTk
import random
import math
import time
from tkinter import messagebox

root = Tk()
root.state("zoomed")
root.resizable(False, False)

img = Image.open("bg11.jpg")
resized = img.resize((1570, 850))
ph = ImageTk.PhotoImage(resized)
l = Label(root, image=ph, fg="red", borderwidth=7, bg="black")
l.place(x=0, y=0)

f2 = Frame(l, bg="orange", width=1535, height=5)
f2.place(x=0, y=0)
f1 = Frame(l, width=1518, height=100, bg="darkblue", borderwidth=5, relief=RIDGE)
f1.place(x=5, y=5)
txtc = str(3)

l1 = Label(f1, text="No of Lives left = " + str(txtc), font=("Algerian", 25, "bold"), bg="darkblue", fg="white",
           borderwidth=5, relief=RIDGE, pady=5, padx=15)
l1.place(x=500, y=20)

f2 = Frame(l, bg="orange", width=1535, height=5)
f2.place(x=0, y=105)

f3 = Frame(l, width=5, height=820, bg="orange")
f3.place(x=0, y=5)

f4 = Frame(l, width=6, height=820, bg="orange")
f4.place(x=1523, y=5)

f2 = Frame(l, bg="orange", width=1535, height=10)
f2.place(x=0, y=825)

velocity = random.randint(1, 50)
angle = random.randint(0, 60)

l2 = Label(l,
           text="Your gun shoots at initial velocity of " + str(velocity) + 'm/s' ".The angle of projectile is " + str(
               angle) + ' degrees.', bg="#c9cdd6", font=("Arial Black", 20, "bold"), fg="black", borderwidth=5,
           relief=RIDGE, padx=15, pady=10)
l2.place(x=120, y=110)

l4 = Label(l, text='How much range should u have from the target?', bg="#c9cdd6", font=("Arial Black", 20, "bold"),
           fg="black", relief=RIDGE, borderwidth=5, padx=15, pady=10)
l4.place(x=400, y=180)

ang = angle * 2
sining = math.sin(math.radians(ang))
sining = abs(sining)
true_range = int(((velocity ** 2) / 10.0) * sining)

txta = StringVar()

txtb = txta.get()

f5 = Frame(l, bg="orange", width=1535, height=5)
f5.place(x=5, y=300)


def check(*args):
    global f1
    global txtc
    global txta
    global ang
    global angle
    global velocity
    txtb = int(txta.get())
    ang = angle * 2
    sining = math.sin(math.radians(ang))
    sining = abs(sining)
    true_range = int(((velocity ** 2) / 9.8) * sining)

    if txtb == int(true_range):
        messagebox.showinfo("CONGRATULATIONS :)", "Correct Answer")
        l = Label(root, image=ph, fg="red", borderwidth=7, bg="black")
        l.place(x=0, y=0)

        f2 = Frame(l, bg="orange", width=1535, height=5)
        f2.place(x=0, y=0)
        f1 = Frame(l, width=1518, height=100, bg="darkblue", borderwidth=5, relief=RIDGE)
        f1.place(x=5, y=5)

        l1 = Label(f1, text="No of Lives Left = " + str(txtc), font=("Algerian", 25, "bold"), bg="darkblue",
                   fg="white", borderwidth=5, relief=RIDGE, pady=5, padx=15)
        l1.place(x=500, y=20)

        f2 = Frame(l, bg="orange", width=1535, height=5)
        f2.place(x=0, y=105)

        f3 = Frame(l, width=5, height=820, bg="orange")
        f3.place(x=0, y=5)

        f4 = Frame(l, width=6, height=820, bg="orange")
        f4.place(x=1523, y=5)

        f2 = Frame(l, bg="orange", width=1535, height=10)
        f2.place(x=0, y=825)

        velocity = random.randint(1, 50)
        angle = random.randint(0, 60)

        l2 = Label(l, text="Your gun shoots at initial velocity of " + str(
            velocity) + 'm/s' ".The angle of projectile is " + str(angle) + ' degrees.', bg="#c9cdd6",
                   font=("Arial Black", 20, "bold"), fg="black", borderwidth=5, relief=RIDGE, padx=15, pady=10)
        l2.place(x=120, y=110)

        l4 = Label(l, text='How much range should u have from the target?', bg="#c9cdd6",
                   font=("Arial Black", 20, "bold"), fg="black", relief=RIDGE, borderwidth=5, padx=15, pady=10)
        l4.place(x=400, y=180)

        ang = angle * 2
        sining = math.sin(math.radians(ang))
        sining = abs(sining)
        true_range = int(((velocity ** 2) / 9.8) * sining)

        txta = StringVar()

        txtb = txta.get()

        f5 = Frame(l, bg="orange", width=1535, height=5)
        f5.place(x=5, y=300)

        def enter1(e):
            user1.delete(0, "end")

        def leave1(e):
            name1 = user1.get()
            if name1 == "":
                user1.insert(0, "  Enter Your Answer           ")

        def check1(*args):
            global f1
            global txtc
            global txta
            global ang
            global angle
            global velocity
            txtb = int(txta.get())
            ang = angle * 2
            sining = math.sin(math.radians(ang))
            sining = abs(sining)
            true_range1 = int(((velocity ** 2) / 9.8) * sining)

            if txtb == int(true_range1):
                messagebox.showinfo("CONGRATS :)", "Correct Answer")
                l = Label(root, image=ph, fg="red", borderwidth=7, bg="black")
                l.place(x=0, y=0)

                f2 = Frame(l, bg="orange", width=1535, height=5)
                f2.place(x=0, y=0)
                f1 = Frame(l, width=1518, height=100, bg="darkblue", borderwidth=5, relief=RIDGE)
                f1.place(x=5, y=5)

                l1 = Label(f1, text="No of Lives Left = " + str(txtc), font=("Algerian", 25, "bold"), bg="darkblue",
                           fg="white", borderwidth=5, relief=RIDGE, pady=5, padx=15)
                l1.place(x=500, y=20)

                f2 = Frame(l, bg="orange", width=1535, height=5)
                f2.place(x=0, y=105)

                f3 = Frame(l, width=5, height=820, bg="orange")
                f3.place(x=0, y=5)

                f4 = Frame(l, width=6, height=820, bg="orange")
                f4.place(x=1523, y=5)

                f2 = Frame(l, bg="orange", width=1535, height=10)
                f2.place(x=0, y=825)

                velocity = random.randint(1, 50)
                angle = random.randint(0, 60)

                l2 = Label(l, text="Your gun shoots at initial velocity of " + str(
                    velocity) + 'm/s' ".The angle of projectile is " + str(angle) + ' degrees.', bg="#c9cdd6",
                           font=("Arial Black", 20, "bold"), fg="black", borderwidth=5, relief=RIDGE, padx=15, pady=10)
                l2.place(x=120, y=110)

                l4 = Label(l, text='How much range should u have from the target?', bg="#c9cdd6",
                           font=("Arial Black", 20, "bold"), fg="black", relief=RIDGE, borderwidth=5, padx=15, pady=10)
                l4.place(x=400, y=180)

                ang = angle * 2
                sining = math.sin(math.radians(ang))
                sining = abs(sining)
                true_range = int(((velocity ** 2) / 9.8) * sining)

                txta = StringVar()

                txtb = txta.get()

                f5 = Frame(l, bg="orange", width=1535, height=5)
                f5.place(x=5, y=300)

                def enter2(e):
                    user2.delete(0, "end")

                def leave2(e):
                    name2 = user2.get()
                    if name2 == "":
                        user2.insert(0, "  Enter Your Answer               ")

                def check2(*args):
                    global f1
                    global txtc
                    global txta
                    global ang
                    global angle
                    global velocity
                    txtb = int(txta.get())
                    ang = angle * 2
                    sining = math.sin(math.radians(ang))
                    sining = abs(sining)
                    true_range2 = int(((velocity ** 2) / 9.8) * sining)

                    if txtb == int(true_range2):
                        messagebox.showinfo("CONGRATS :)", "Correct Answer")
                        l = Label(root, image=ph, fg="red", borderwidth=7, bg="black")
                        l.place(x=0, y=0)

                        f2 = Frame(l, bg="orange", width=1535, height=5)
                        f2.place(x=0, y=0)
                        f1 = Frame(l, width=1518, height=100, bg="darkblue", borderwidth=5, relief=RIDGE)
                        f1.place(x=5, y=5)

                        l1 = Label(f1, text="No of Lives Left = " + str(txtc), font=("Algerian", 25, "bold"),
                                   bg="darkblue",
                                   fg="white", borderwidth=5, relief=RIDGE, pady=5, padx=15)
                        l1.place(x=500, y=20)

                        f2 = Frame(l, bg="orange", width=1535, height=5)
                        f2.place(x=0, y=105)

                        f3 = Frame(l, width=5, height=820, bg="orange")
                        f3.place(x=0, y=5)

                        f4 = Frame(l, width=6, height=820, bg="orange")
                        f4.place(x=1523, y=5)

                        f2 = Frame(l, bg="orange", width=1535, height=10)
                        f2.place(x=0, y=825)

                        velocity = random.randint(1, 50)
                        angle = random.randint(0, 60)

                        l2 = Label(l, text="Your gun shoots at an initial velocity of " + str(
                            velocity) + 'm/s' ".The angle of projectile is " + str(angle) + ' degrees.', bg="#c9cdd6",
                                   font=("Arial Black", 20, "bold"), fg="black", borderwidth=5, relief=RIDGE, padx=15,
                                   pady=10)
                        l2.place(x=120, y=110)

                        l4 = Label(l, text='How much range should u have from the target?', bg="#c9cdd6",
                                   font=("Arial Black", 20, "bold"), fg="black", relief=RIDGE, borderwidth=5, padx=15,
                                   pady=10)
                        l4.place(x=400, y=180)

                        ang = angle * 2
                        sining = math.sin(math.radians(ang))
                        sining = abs(sining)
                        true_range = int(((velocity ** 2) / 9.8) * sining)

                        txta = StringVar()

                        txtb = txta.get()

                        f5 = Frame(l, bg="orange", width=1535, height=5)
                        f5.place(x=5, y=300)

                        def enter3(e):
                            user3.delete(0, "end")

                        def leave3(e):
                            name3 = user3.get()
                            if name3 == "":
                                user3.insert(0, "  Enter Your Answer               ")

                        def check3(*args):
                            global f1
                            global txtc
                            global txta
                            global ang
                            global angle
                            global velocity
                            txtb = int(txta.get())
                            ang = angle * 2
                            sining = math.sin(math.radians(ang))
                            sining = abs(sining)
                            true_range4 = int(((velocity ** 2) / 9.8) * sining)

                            if txtb == int(true_range4):
                                messagebox.showinfo("CONGRATS :)", "You have entered LEVEL 2")
                                l = Label(root, image=ph, fg="red", borderwidth=7, bg="black")
                                l.place(x=0, y=0)

                                f1 = Frame(root, bg="darkblue", width=1540, height=10)
                                f1.place(x=0, y=0)

                                f2 = Frame(l, bg="darkblue", width=1535, height=5)
                                f2.place(x=0, y=105)

                                f3 = Frame(root, width=7, height=820, bg="darkblue")
                                f3.place(x=0, y=5)

                                f4 = Frame(l, width=6, height=820, bg="darkblue")
                                f4.place(x=1523, y=5)

                                f2 = Frame(l, bg="darkblue", width=1535, height=10)
                                f2.place(x=0, y=825)
                                txtc = str(2)

                                l1 = Label(l, text="No of Lives left = " + str(txtc), font=("Algerian", 25, "bold"),
                                           bg="darkblue", fg="white",
                                           borderwidth=5, relief=RIDGE, padx=609, pady=25)
                                l1.place(x=4, y=5)

                                velocity = random.randint(1, 50)
                                angle = random.randint(0, 60)

                                l2 = Label(l, text="Your gun shoots at initial velocity of " + str(
                                    velocity) + 'm/s' ".The angle of projectile is " + str(angle) + ' degrees.'
                                           , bg="#c9cdd6", font=("Arial Black", 20, "bold"), fg="black", borderwidth=5,
                                           relief=RIDGE, padx=15, pady=10)
                                l2.place(x=120, y=110)

                                l4 = Label(l, text='How much range should u have from the target?', bg="#c9cdd6",
                                           font=("Arial Black", 20, "bold"), fg="black", relief=RIDGE, borderwidth=5,
                                           padx=15, pady=10)
                                l4.place(x=400, y=180)

                                l6 = Label(l, text='&', bg="#c9cdd6", font=("Arial Black", 20, "bold"), fg="black",
                                           relief=RIDGE, borderwidth=5, padx=15, pady=10)
                                l6.place(x=700, y=330)

                                l5 = Label(l, text="Enter your answer for time of flight", bg="#c9cdd6",
                                           font=("Arial Black", 20, "bold"), fg="black", relief=RIDGE, borderwidth=5,
                                           padx=15, pady=10)
                                l5.place(x=450, y=400)
                                txte = StringVar()
                                txtf = StringVar()

                                def check5(*args):
                                    global txtc
                                    txtx = int(txte.get())
                                    txty = int(txtf.get())

                                    global txta
                                    global ang
                                    global angle
                                    global velocity

                                    ang = angle * 2
                                    sining = math.sin(math.radians(ang))
                                    sining = abs(sining)
                                    true_range = int(((velocity ** 2) / 9.8) * sining)
                                    T = 2 * (velocity * (math.sin(math.radians(angle)))) / (9.8)

                                    if txtx == int(true_range) and txty == int(T):
                                        messagebox.showinfo("CONGRATS :)", "Correct Answer")
                                        l = Label(root, image=ph, fg="red", borderwidth=7, bg="black")
                                        l.place(x=0, y=0)

                                        f1 = Frame(root, bg="darkblue", width=1540, height=10)
                                        f1.place(x=0, y=0)

                                        f2 = Frame(l, bg="darkblue", width=1535, height=5)
                                        f2.place(x=0, y=105)

                                        f3 = Frame(root, width=7, height=820, bg="darkblue")
                                        f3.place(x=0, y=5)

                                        f4 = Frame(l, width=6, height=820, bg="darkblue")
                                        f4.place(x=1523, y=5)

                                        f2 = Frame(l, bg="darkblue", width=1535, height=10)
                                        f2.place(x=0, y=825)
                                        l1 = Label(l, text="No of Lives left = " + str(txtc),
                                                   font=("Algerian", 25, "bold"), bg="darkblue", fg="white",
                                                   borderwidth=5, relief=RIDGE, padx=609, pady=25)
                                        l1.place(x=4, y=5)

                                        velocity = random.randint(1, 50)
                                        angle = random.randint(0, 60)

                                        l2 = Label(l, text="Your gun shoots at initial velocity of " + str(
                                            velocity) + 'm/s' ".The angle of projectile is " + str(angle) + ' degrees.'
                                                   , bg="#c9cdd6", font=("Arial Black", 20, "bold"), fg="black",
                                                   borderwidth=5, relief=RIDGE, padx=15,
                                                   pady=10)
                                        l2.place(x=120, y=110)

                                        l4 = Label(l, text='How much range should u have from the target?',
                                                   bg="#c9cdd6",
                                                   font=("Arial Black", 20, "bold"), fg="black", relief=RIDGE,
                                                   borderwidth=5, padx=15, pady=10)
                                        l4.place(x=400, y=180)

                                        l6 = Label(l, text='&', bg="#c9cdd6", font=("Arial Black", 20, "bold"),
                                                   fg="black", relief=RIDGE, borderwidth=5,
                                                   padx=15, pady=10)
                                        l6.place(x=700, y=330)

                                        l5 = Label(l, text="Enter your answer for time of flight", bg="#c9cdd6",
                                                   font=("Arial Black", 20, "bold"),
                                                   fg="black", relief=RIDGE, borderwidth=5, padx=15, pady=10)
                                        l5.place(x=450, y=400)

                                        # f11=Frame(l,bg="black", borderwidth=0, height=2, width=2)
                                        def check6(*args):
                                            global txtc
                                            txtx = int(txte.get())
                                            txty = int(txtf.get())

                                            global txta
                                            global ang
                                            global angle
                                            global velocity

                                            ang = angle * 2
                                            sining = math.sin(math.radians(ang))
                                            sining = abs(sining)
                                            true_range1 = int(((velocity ** 2) / 9.8) * sining)
                                            T1 = 2 * (velocity * (math.sin(math.radians(angle)))) / (9.8)

                                            if txtx == int(true_range1) and txty == int(T1):

                                                messagebox.showinfo("CONGRATS :)", "Correct Answer")
                                                l = Label(root, image=ph, fg="red", borderwidth=7, bg="black")
                                                l.place(x=0, y=0)

                                                f1 = Frame(root, bg="darkblue", width=1540, height=10)
                                                f1.place(x=0, y=0)

                                                f2 = Frame(l, bg="darkblue", width=1535, height=5)
                                                f2.place(x=0, y=105)

                                                f3 = Frame(root, width=7, height=820, bg="darkblue")
                                                f3.place(x=0, y=5)

                                                f4 = Frame(l, width=6, height=820, bg="darkblue")
                                                f4.place(x=1523, y=5)

                                                f2 = Frame(l, bg="darkblue", width=1535, height=10)
                                                f2.place(x=0, y=825)
                                                l1 = Label(l, text="No of Lives left = " + str(txtc),
                                                           font=("Algerian", 25, "bold"), bg="darkblue",
                                                           fg="white",
                                                           borderwidth=5, relief=RIDGE, padx=609, pady=25)
                                                l1.place(x=4, y=5)

                                                velocity = random.randint(1, 50)
                                                angle = random.randint(0, 60)

                                                l2 = Label(l, text="Your gun shoots at initial velocity of " + str(
                                                    velocity) + 'm/s' ".The angle of projectile is " + str(
                                                    angle) + ' degrees.'
                                                           , bg="#c9cdd6", font=("Arial Black", 20, "bold"), fg="black",
                                                           borderwidth=5, relief=RIDGE,
                                                           padx=15,
                                                           pady=10)
                                                l2.place(x=120, y=110)

                                                l4 = Label(l, text='How much range should u have from the target?',
                                                           bg="#c9cdd6",
                                                           font=("Arial Black", 20, "bold"), fg="black", relief=RIDGE,
                                                           borderwidth=5, padx=15, pady=10)
                                                l4.place(x=400, y=180)

                                                l6 = Label(l, text='&', bg="#c9cdd6", font=("Arial Black", 20, "bold"),
                                                           fg="black", relief=RIDGE,
                                                           borderwidth=5,
                                                           padx=15, pady=10)
                                                l6.place(x=700, y=330)

                                                l5 = Label(l, text="Enter your answer for time of flight", bg="#c9cdd6",
                                                           font=("Arial Black", 20, "bold"),
                                                           fg="black", relief=RIDGE, borderwidth=5, padx=15, pady=10)
                                                l5.place(x=450, y=400)

                                                def check7(*args):
                                                    global txtc
                                                    txtx = int(txte.get())
                                                    txty = int(txtf.get())

                                                    global txta
                                                    global ang
                                                    global angle
                                                    global velocity

                                                    ang = angle * 2
                                                    sining = math.sin(math.radians(ang))
                                                    sining = abs(sining)
                                                    true_range2 = int(((velocity ** 2) / 9.8) * sining)
                                                    T2 = 2 * (velocity * (math.sin(math.radians(angle)))) / (9.8)

                                                    if txtx == int(true_range2) and txty == int(T2):
                                                        messagebox.showinfo("CONGRATS :)", "Correct Answer")
                                                        l = Label(root, image=ph, fg="red", borderwidth=7, bg="black")
                                                        l.place(x=0, y=0)

                                                        f1 = Frame(root, bg="darkblue", width=1540, height=10)
                                                        f1.place(x=0, y=0)

                                                        f2 = Frame(l, bg="darkblue", width=1535, height=5)
                                                        f2.place(x=0, y=105)

                                                        f3 = Frame(root, width=7, height=820, bg="darkblue")
                                                        f3.place(x=0, y=5)

                                                        f4 = Frame(l, width=6, height=820, bg="darkblue")
                                                        f4.place(x=1523, y=5)

                                                        f2 = Frame(l, bg="darkblue", width=1535, height=10)
                                                        f2.place(x=0, y=825)
                                                        l1 = Label(l, text="No of Lives left = " + str(txtc),
                                                                   font=("Algerian", 25, "bold"),
                                                                   bg="darkblue", fg="white",
                                                                   borderwidth=5, relief=RIDGE, padx=609, pady=25)
                                                        l1.place(x=4, y=5)

                                                        velocity = random.randint(1, 50)
                                                        angle = random.randint(0, 60)

                                                        l2 = Label(l,
                                                                   text="Your gun shoots at initial velocity of " + str(
                                                                       velocity) + 'm/s' ".The angle of projectile is " + str(
                                                                       angle) + ' degrees.'
                                                                   , bg="#c9cdd6", font=("Arial Black", 20, "bold"),
                                                                   fg="black", borderwidth=5,
                                                                   relief=RIDGE,
                                                                   padx=15,
                                                                   pady=10)
                                                        l2.place(x=120, y=110)

                                                        l4 = Label(l,
                                                                   text='How much range should u have from the target?',
                                                                   bg="#c9cdd6",
                                                                   font=("Arial Black", 20, "bold"), fg="black",
                                                                   relief=RIDGE, borderwidth=5, padx=15,
                                                                   pady=10)
                                                        l4.place(x=400, y=180)

                                                        l6 = Label(l, text='&', bg="#c9cdd6",
                                                                   font=("Arial Black", 20, "bold"), fg="black",
                                                                   relief=RIDGE,
                                                                   borderwidth=5,
                                                                   padx=15, pady=10)
                                                        l6.place(x=700, y=330)

                                                        l5 = Label(l, text="Enter your answer for time of flight",
                                                                   bg="#c9cdd6",
                                                                   font=("Arial Black", 20, "bold"),
                                                                   fg="black", relief=RIDGE, borderwidth=5, padx=15,
                                                                   pady=10)
                                                        l5.place(x=450, y=400)

                                                        def check8(*args):
                                                            global txtc
                                                            txtx = int(txte.get())
                                                            txty = int(txtf.get())

                                                            global txta
                                                            global ang
                                                            global angle
                                                            global velocity

                                                            ang = angle * 2
                                                            sining = math.sin(math.radians(ang))
                                                            sining = abs(sining)
                                                            true_range3 = int(((velocity ** 2) / 9.8) * sining)
                                                            T3 = 2 * (velocity * (math.sin(math.radians(angle)))) / (
                                                                9.8)

                                                            if txtx == int(true_range3) and txty == int(T3):
                                                                z = Toplevel(root)
                                                                z.state('zoomed')
                                                                L = Label(z,
                                                                          text="Congratulations you have won the game ",
                                                                          font="Algerian 40 bold", bg="grey").place(
                                                                    x=300, y=400)
                                                                z.mainloop()


                                                            else:
                                                                messagebox.showinfo("OH!", "Incorrect Answer")

                                                                if txtc == 0:
                                                                    messagebox.showinfo("OH!", "You lost ")
                                                                    root.destroy()
                                                                else:
                                                                    txtc = int(txtc)
                                                                    txtc = txtc - 1
                                                                    l1 = Label(root,
                                                                               text="No of Lives left = " + str(txtc),
                                                                               font=("Algerian", 25, "bold"),
                                                                               bg="darkblue", fg="white",
                                                                               borderwidth=5, relief=RIDGE, padx=609,
                                                                               pady=25)
                                                                    l1.place(x=4, y=5)

                                                        def enter(e):
                                                            user.delete(0, "end")

                                                        def leave(e):
                                                            name = user.get()
                                                            if name == "":
                                                                user.insert(0, "  Enter Your Answer          ")

                                                        user = Entry(l, fg="black", bg="white", width=18,
                                                                     font=("Century Gothic", 19), borderwidth=5,
                                                                     relief=RIDGE,
                                                                     textvariable=txte)
                                                        user.place(x=600, y=280)
                                                        user.insert(0, "  Enter Your Answer           ")
                                                        user.bind('<Return>', check8)
                                                        user.bind("<FocusIn>", enter)
                                                        user.bind("<FocusOut>", leave)

                                                        def enter2(e):
                                                            user2.delete(0, "end")

                                                        def leave2(e):
                                                            name2 = user2.get()
                                                            if name2 == "":
                                                                user2.insert(0, "  Enter Your Answer         ")

                                                        user2 = Entry(l, fg="black", bg="white", width=18,
                                                                      font=("Century Gothic", 19), borderwidth=5,
                                                                      relief=RIDGE,
                                                                      textvariable=txtf)
                                                        user2.place(x=600, y=480)
                                                        user2.insert(0, "  Enter Your Answer            ")
                                                        user2.bind('<Return>', check8)
                                                        user2.bind("<FocusIn>", enter2)
                                                        user2.bind("<FocusOut>", leave2)


                                                    else:
                                                        messagebox.showinfo("OH!", "Incorrect Answer")

                                                        if txtc == 0:
                                                            messagebox.showinfo("OH!", "You lost ")
                                                            b.destroy()
                                                        else:
                                                            txtc = int(txtc)
                                                            txtc = txtc - 1
                                                            l1 = Label(root, text="No of Lives left = " + str(txtc),
                                                                       font=("Algerian", 25, "bold"),
                                                                       bg="darkblue", fg="white",
                                                                       borderwidth=5, relief=RIDGE, padx=609, pady=25)
                                                            l1.place(x=4, y=5)

                                                def enter(e):
                                                    user.delete(0, "end")

                                                def leave(e):
                                                    name = user.get()
                                                    if name == "":
                                                        user.insert(0, "  Enter Your Answer         ")

                                                user = Entry(l, fg="black", bg="white", width=18,
                                                             font=("Century Gothic", 19), borderwidth=5,
                                                             relief=RIDGE,
                                                             textvariable=txte)
                                                user.place(x=600, y=280)
                                                user.insert(0, "  Enter Your Answer            ")
                                                user.bind('<Return>', check7)
                                                user.bind("<FocusIn>", enter)
                                                user.bind("<FocusOut>", leave)

                                                def enter2(e):
                                                    user2.delete(0, "end")

                                                def leave2(e):
                                                    name2 = user2.get()
                                                    if name2 == "":
                                                        user2.insert(0, "  Enter Your Answer         ")

                                                user2 = Entry(l, fg="black", bg="white", width=18,
                                                              font=("Century Gothic", 19), borderwidth=5,
                                                              relief=RIDGE,
                                                              textvariable=txtf)
                                                user2.place(x=600, y=480)
                                                user2.insert(0, "  Enter Your Answer            ")
                                                user2.bind('<Return>', check7)
                                                user2.bind("<FocusIn>", enter2)
                                                user2.bind("<FocusOut>", leave2)


                                            else:
                                                messagebox.showinfo("OH!", "Incorrect Answer")

                                                if txtc == 0:
                                                    messagebox.showinfo("OH!", "You lost")
                                                    root.destroy()
                                                else:
                                                    txtc = int(txtc)
                                                    txtc = txtc - 1
                                                    l1 = Label(root, text="No of Lives left = " + str(txtc),
                                                               font=("Algerian", 25, "bold"), bg="darkblue",
                                                               fg="white",
                                                               borderwidth=5, relief=RIDGE, padx=609, pady=25)
                                                    l1.place(x=4, y=5)

                                        def enter(e):
                                            user.delete(0, "end")

                                        def leave(e):
                                            name = user.get()
                                            if name == "":
                                                user.insert(0, "  Enter Your Answer         ")

                                        user = Entry(l, fg="black", bg="white", width=18, font=("Century Gothic", 19),
                                                     borderwidth=5, relief=RIDGE,
                                                     textvariable=txte)
                                        user.place(x=600, y=280)
                                        user.insert(0, "  Enter Your Answer        ")
                                        user.bind('<Return>', check6)
                                        user.bind("<FocusIn>", enter)
                                        user.bind("<FocusOut>", leave)

                                        def enter2(e):
                                            user2.delete(0, "end")

                                        def leave2(e):
                                            name2 = user2.get()
                                            if name2 == "":
                                                user2.insert(0, "  Enter Your Answer           ")

                                        user2 = Entry(l, fg="black", bg="white", width=18, font=("Century Gothic", 19),
                                                      borderwidth=5, relief=RIDGE,
                                                      textvariable=txtf)
                                        user2.place(x=600, y=480)
                                        user2.insert(0, "  Enter Your Answer           ")
                                        user2.bind('<Return>', check6)
                                        user2.bind("<FocusIn>", enter2)
                                        user2.bind("<FocusOut>", leave2)


                                    else:
                                        messagebox.showinfo("OH!", "Incorrect Answer")

                                        if txtc == 0:
                                            messagebox.showinfo("OH!", "You lost ")
                                            root.destroy()
                                        else:
                                            txtc = int(txtc)
                                            txtc = txtc - 1
                                            l1 = Label(root, text="No of Lives left = " + str(txtc),
                                                       font=("Algerian", 25, "bold"), bg="darkblue",
                                                       fg="white",
                                                       borderwidth=5, relief=RIDGE, padx=609, pady=25)
                                            l1.place(x=4, y=5)

                                def enter(e):
                                    user.delete(0, "end")

                                def leave(e):
                                    name = user.get()
                                    if name == "":
                                        user.insert(0, "  Enter Your Answer          ")

                                user = Entry(l, fg="black", bg="white", width=18, font=("Century Gothic", 19),
                                             borderwidth=5, relief=RIDGE,
                                             textvariable=txte)
                                user.place(x=600, y=280)
                                user.insert(0, "  Enter Your Answer          ")
                                user.bind('<Return>', check5)
                                user.bind("<FocusIn>", enter)
                                user.bind("<FocusOut>", leave)

                                def enter2(e):
                                    user2.delete(0, "end")

                                def leave2(e):
                                    name2 = user2.get()
                                    if name2 == "":
                                        user2.insert(0, "  Enter Your Answer             ")

                                user2 = Entry(l, fg="black", bg="white", width=18, font=("Century Gothic", 19),
                                              borderwidth=5, relief=RIDGE,
                                              textvariable=txtf)
                                user2.place(x=600, y=480)
                                user2.insert(0, "  Enter Your Answer           ")
                                user2.bind('<Return>', check5)
                                user2.bind("<FocusIn>", enter2)
                                user2.bind("<FocusOut>", leave2)

                            else:

                                messagebox.showinfo("ALERT!", "Wrong answer")
                                if txtc == 0:
                                    messagebox.showinfo("Alert", "You lost the game")
                                    root.destroy()
                                else:
                                    txtc = int(txtc)
                                    txtc = txtc - 1
                                    l1 = Label(f1, text="No of Lives Left = " + str(txtc),
                                               font=("Algerian", 25, "bold"), bg="darkblue",
                                               fg="white", borderwidth=5, relief=RIDGE, pady=5, padx=15)
                                    l1.place(x=500, y=20)

                        user3 = Entry(l, fg="black", bg="white", width=18, font=("Century Gothic", 19), borderwidth=5,
                                      relief=RIDGE,
                                      textvariable=txta)
                        user3.place(x=600, y=250)
                        user3.insert(0, "  Enter Your Answer                      ")
                        user3.bind('<Return>', check3)
                        user3.bind("<FocusIn>", enter3)
                        user3.bind("<FocusOut>", leave3)
                    else:

                        messagebox.showinfo("ALERT!", "Wrong Answer")
                        if txtc == 0:
                            messagebox.showinfo("Alert", "You lost the game")
                            root.destroy()
                        else:
                            txtc = int(txtc)
                            txtc = txtc - 1
                            l1 = Label(f1, text="No of Lives Left = " + str(txtc), font=("Algerian", 25, "bold"),
                                       bg="darkblue",
                                       fg="white", borderwidth=5, relief=RIDGE, pady=5, padx=15)
                            l1.place(x=500, y=20)

                user2 = Entry(l, fg="black", bg="white", width=18, font=("Century Gothic", 19), borderwidth=5,
                              relief=RIDGE,
                              textvariable=txta)
                user2.place(x=600, y=250)
                user2.insert(0, "  Enter Your Answer                ")
                user2.bind('<Return>', check2)
                user2.bind("<FocusIn>", enter2)
                user2.bind("<FocusOut>", leave2)
            else:

                messagebox.showinfo("ALERT!", "Wrong Answer                  ")
                if txtc == 0:
                    messagebox.showinfo("Alert", "You lost the game")
                    root.destroy()
                else:
                    txtc = int(txtc)
                    txtc = txtc - 1
                    l1 = Label(f1, text="No of Lives Left = " + str(txtc), font=("Algerian", 25, "bold"), bg="darkblue",
                               fg="white", borderwidth=5, relief=RIDGE, pady=5, padx=15)
                    l1.place(x=500, y=20)

        user1 = Entry(l, fg="black", bg="white", width=18, font=("Century Gothic", 19), borderwidth=5, relief=RIDGE,
                     textvariable=txta)
        user1.place(x=600, y=250)
        user1.insert(0, "  Enter Your Answer                  ")
        user1.bind('<Return>', check1)
        user1.bind("<FocusIn>", enter1)
        user1.bind("<FocusOut>", leave1)

    else:

        messagebox.showinfo("ALERT!", "Wrong Answer                ")
        if txtc == 0:
            messagebox.showinfo("Alert", "You Lost the game ")
            root.destroy()
        else:
            txtc = int(txtc)
            txtc = txtc - 1
            l1 = Label(f1, text="No of Lives Left = " + str(txtc), font=("Algerian", 25, "bold"), bg="darkblue",
                       fg="white", borderwidth=5, relief=RIDGE, pady=5, padx=15)
            l1.place(x=500, y=20)


def enter(e):
    user.delete(0, "end")


def leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "  Enter Your Answer                      ")


user = Entry(l, fg="black", bg="white", width=18, font=("Century Gothic", 19), borderwidth=5, relief=RIDGE,
             textvariable=txta)
user.place(x=600, y=250)
user.insert(0, "  Enter Your Answer")
user.bind('<Return>', check)
user.bind("<FocusIn>", enter)
user.bind("<FocusOut>", leave)

root.mainloop()


# In[ ]:





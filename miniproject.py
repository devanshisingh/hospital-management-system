from tkinter import *
import mysql.connector

win=Tk()
win.title('User Login')
con = mysql.connector.connect(host="localhost", user='devanshi',
                              passwd = 'Divdev!2', database = 'hospital')
cur = con.cursor(prepared=True)
   
def menu():
    win.title('Welcome Admin')
    
    f=Frame(win, height=300, width=400)
    
    def register():
        win.title('Register New Patient')
        f.destroy()
        f1=Frame(win, height=400, width=400)
       
        cur.execute("Select count(pid) from Patient;")
        cnt = cur.fetchone()[0]
        pid = cnt+1
        plabel = Label(f1, text = 'Patient Id.').place(x=25, y=25)
        plabel1 = Label(f1, text = pid).place(x=100, y=25)
        
        name=StringVar()
        nlabel = Label(f1, text = 'Full Name').place(x=25, y=65)
        nentry = Entry(f1, textvariable = name, width = 30).place(x=100, y=65)

        age = IntVar()
        alabel = Label(f1, text = 'Age').place(x=25, y=105)
        aentry = Entry(f1, textvariable= age, width = 5).place(x=100, y=105)
        
        weight = IntVar()
        wlabel = Label(f1, text = 'Weight').place(x=175, y=105)
        wentry = Entry(f1, textvariable = weight, width = 5).place(x=250, y=105)
        
        gender = StringVar()
        glabel = Label(f1, text = 'Gender').place(x=25, y=145)
        m = Radiobutton(f1, text = 'Male', variable = gender,
                        value = 'Male').place(x=100, y=145)
        fm = Radiobutton(f1, text = 'Female', variable = gender,
                         value = 'Female').place(x=185, y=145)
        othr = Radiobutton(f1, text = 'Other', variable = gender,
                           value = 'Other').place(x=270, y=145)
        
        add = StringVar()
        adlabel = Label(f1, text = 'Address').place(x=25, y=185)
        adentry = Entry(f1, textvariable = add).place(x=100, y=185)
        
        phone = IntVar()
        plabel = Label(f1, text = 'Phone no.').place(x=25, y=225)
        pentry = Entry(f1, textvariable = phone).place(x=100, y=225)
        
        disease = StringVar()
        dlabel = Label(f1, text = 'Disease').place(x=25, y=265)
        dentry = Entry(f1, textvariable = disease).place(x=100, y=265)

        docid = StringVar()
        dilabel = Label(f1, text = 'Doctor Id.').place(x=25, y=305)
        dientry = Entry(f1, textvariable = docid).place(x=100, y=305)

        def back():
            f1.destroy()
            menu()
        b1 = Button(f1, text='Back', command=back).place(x=25, y=345)
        b2 = Button(f1, text='Quit',command=win.quit).place(x=110, y=345)

        def clear():
            name.set('')
            age.set('')
            weight.set('')
            gender.set('')
            add.set('')
            phone.set('')
            disease.set('')
            docid.set('')
        b3 = Button(f1, text='Clear',command=clear).place(x=195, y=345)

        def submit():
            cur.execute("INSERT INTO Patient VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (pid, name.get(), age.get(), weight.get(), gender.get(), add.get(),
                         phone.get(), disease.get(), docid.get()))
            con.commit()
            back()
            
        b4 = Button(f1, text='Submit',command=submit).place(x=280, y=345)
        f1.pack()
    
    B1 = Button(f, text = 'Register new patient', command=register).place(x = 25, y = 50)

    def bill():
        win.title('Get Bill')
        f.destroy()
        f2 = Frame(win, height = 600, width = 400)

        cur.execute("Select count(bill_no) from Bill;")
        cnt = cur.fetchone()[0]
        bno = cnt+1
        plabel = Label(f2, text = 'Bill No.').place(x=25, y=25)
        plabel1 = Label(f2, text = bno).place(x=140, y=25)
        
        pid = StringVar()
        nlabel = Label(f2, text = 'Patient Id.').place(x=25, y=65)
        nentry = Entry(f2, textvariable = pid, width = 5).place(x=140, y=65)

        def back():
            f2.destroy()
            menu()
        b1 = Button(f2, text = 'Back', command = back).place(x=75, y=105)

        def fetch():
            cur.execute("SELECT doctorid from Patient where pid=(%s)",(pid.get()))
            pt = cur.fetchone()[0]
            pt=str(pt)
            if 'ORTH1' in pt:
                pt='ORTH'
            elif 'GYN01' in pt or 'GYN02' in pt:
                pt = 'GYN'
            elif 'CARD1' in pt or 'CARD2' in pt:
                pt = 'CARD'
            else:
                pt = 'ONC'
            alabel = Label(f2, text = 'Patient Type').place(x=25, y=145)
            aentry = Label(f2, text = pt).place(x=140, y=145)

            doc_chg = IntVar()
            wlabel = Label(f2, text = 'Doctor Charge').place(x=25, y=185)
            wentry = Entry(f2, textvariable = doc_chg, width = 5).place(x=140, y=185)
            
            med_chg = IntVar()
            glabel = Label(f2, text = 'Medical charge').place(x=25, y=225)
            gentry = Entry(f2, textvariable = med_chg).place(x=140, y=225)
            
            room_chg = IntVar()
            rlabel = Label(f2, text = 'Room charge').place(x=25, y=265)
            rentry = Entry(f2, textvariable = room_chg).place(x=140, y=265)
            
            op_chg = IntVar()
            plabel = Label(f2, text = 'Operation charge').place(x=25, y=305)
            pentry = Entry(f2, textvariable = op_chg).place(x=140, y=305)

            cur.execute("select date_of_dis - date_of_adm from Inpatient where pid=(%s)",
                        (pid.get()))
            dy = cur.fetchone()[0]
            dlabel = Label(f2, text = 'Days').place(x=25, y=345)
            dentry = Label(f2, text = dy).place(x=140, y=345)

            nur_chg = IntVar()
            dilabel = Label(f2, text = 'Nursing charge').place(x=25, y=385)
            dientry = Entry(f2, textvariable = nur_chg).place(x=140, y=385)

            adv = IntVar()
            dilabel = Label(f2, text = 'Advance').place(x=25, y=425)
            dientry = Entry(f2, textvariable = adv).place(x=140, y=425)

            health_card = StringVar()
            dilabel = Label(f2, text = 'Health Card').place(x=25, y=465)
            dientry = Entry(f2, textvariable = health_card).place(x=140, y=465)

            llabel = Label(f2, text = 'Lab Charge').place(x=25, y=505)
            cur.execute('select sum(amount) from Lab where pid=(%s)',pid.get())
            lab = int(cur.fetchone()[0])
            lentry = Label(f2, text = lab).place(x=140, y=505)

            def submit():
                doc = doc_chg.get()
                med = med_chg.get()
                bill = int(doc_chg.get() + med_chg.get() + room_chg.get() + op_chg.get() + nur_chg.get()
                           - adv.get()) + lab
                cur.execute("INSERT INTO Bill VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (bno, pid.get(), pt, doc, med, room_chg.get(), op_chg.get(), dy,
                         nur_chg.get(), adv.get(), health_card.get(), lab, bill))
                con.commit()
                w = Tk()
                w.title('Bill')
                w.geometry('300x550')
                c='mistyrose'
                w.configure(bg=c)
                label1 = Label(w, text = 'Bill no.', bg=c).place(x=25, y=30)
                label2 = Label(w, text = bno, bg=c).place(x=150, y=30)
                label1 = Label(w, text = 'Patient Id.', bg=c).place(x=25, y=70)
                label2 = Label(w, text = pid.get(), bg=c).place(x=150, y=70)
                label1 = Label(w, text = 'Patient Type', bg=c).place(x=25, y=110)
                label2 = Label(w, text = pt, bg=c).place(x=150, y=110)
                label1 = Label(w, text = 'Doctor Charge', bg=c).place(x=25, y=150)
                label2 = Label(w, text = doc, bg=c).place(x=150, y=150)
                label1 = Label(w, text = 'Medical Charge', bg=c).place(x=25, y=190)
                label2 = Label(w, text = med, bg=c).place(x=150, y=190)
                label1 = Label(w, text = 'Room charge', bg=c).place(x=25, y=230)
                label2 = Label(w, text = room_chg.get(), bg=c).place(x=150, y=230)
                label1 = Label(w, text = 'Operation Charge', bg=c).place(x=25, y=270)
                label2 = Label(w, text = op_chg.get(), bg=c).place(x=150, y=270)
                label1 = Label(w, text = 'No of Days', bg=c).place(x=25, y=310)
                label2 = Label(w, text = dy, bg=c).place(x=150, y=310)
                label1 = Label(w, text = 'Nursing Charge', bg=c).place(x=25, y=350)
                label2 = Label(w, text = nur_chg.get(), bg=c).place(x=150, y=350)
                label1 = Label(w, text = 'Advance', bg=c).place(x=25, y=390)
                label2 = Label(w, text = adv.get(), bg=c).place(x=150, y=390)
                label1 = Label(w, text = 'Health Card', bg=c).place(x=25, y=430)
                label2 = Label(w, text = health_card.get(), bg=c).place(x=150, y=430)
                label1 = Label(w, text = 'Lab Charge', bg=c).place(x=25, y=470)
                label2 = Label(w, text = lab, bg=c).place(x=150, y=470)
                label1 = Label(w, text = 'Bill', font = 70, bg=c).place(x=25, y=510)
                label2 = Label(w, text = bill, font = 70, bg=c).place(x=150, y=510)
                w.mainloop()

                cur.execute('Delete from Patient where pid = (%s)',(pid.get(), ))
                cur.execute('Delete from Lab where pid = (%s)',(pid.get(), ))
                #cur.execute('Delete from 
                
                back()

            b = Button(f2, text = 'Submit', command = submit).place(x=175, y=545)
    
        b2 = Button(f2, text = 'Go', command=fetch).place(x=175, y=105)

        
        f2.pack()

    B2 = Button(f, text = 'Get Bill', command=bill).place(x=25, y=100)

    def room():
        win.title('Available Rooms')
        f.destroy()
        f3 = Frame(win, height=400, width = 400)

        label = Label(f3, text = 'Room No.').place(x=25, y=30)
        label = Label(f3, text = 'Room type').place(x=150, y=30)

        cur.execute('select * from Room where status = (%s) order by room_no',('Available', ))
        i=0
            
        for row in cur:
            label = Label(f3, text = int(row[0])).place(x=25, y=70+i*25)
            if 'Medium' in str(row[1]):
                rt = 'Medium'
            elif 'Simple' in str(row[1]):
                rt = 'Simple'
            else:
                rt = 'Deluxe'
            label = Label(f3, text = rt).place(x=150, y=70+i*25)
            i+=1
                
##        pid = StringVar()
##        label = Label(f3, text = 'Patient Id.').place(x=25, y=70 + (i+1)*40)
##        entry = Entry(f3, textvariable = pid, width=5).place(x=140, y=70+(i+1)*40)

        rno = StringVar()
        label = Label(f3, text = 'Take Room no.').place(x=25, y=70+(i+1)*40)
        entry = Entry(f3, textvariable = rno, width = 5).place(x=140, y=70+(i+1)*40)
        i=0
        
        def back():
            f3.destroy()
            menu()
        b = Button(f3, text = 'Back', command=back).place(x=75, y=300)

        def submit():
            cur.execute('update Room set status = (%s) where room_no = (%s)', ('Occupied', rno.get()))
            con.commit()
            back()
        b1 = Button(f3, text = 'Submit', command=submit).place(x=150, y=300)
        f3.pack()
                
    B3 = Button(f, text = 'Available Rooms', command=room).place(
        x = 25, y = 150)


    def delrec():
        win.title('Delete a record')
        f.destroy()
        f4 = Frame(win, height = 300, width = 300)
        pid = StringVar()
        nlabel = Label(f4, text = 'Patient Id.').place(x=25, y=65)
        nentry = Entry(f4, textvariable = pid, width = 5).place(x=140, y=65)

        def delete():
            cur.execute('delete from Patient where pid = (%s)',(pid.get()))
            cur.execute('delete from Lab where pid = (%s)', (pid.get()))
            con.commit()
            l=Label(f4, text = 'Record Deleted!').place(x=75, y=150)
        b=Button(f4, text = 'Delete', command=delete).place(x=170, y=115)

        def back():
            f4.destroy()
            menu()
        bk = Button(f4, text = 'Back', command=back).place(x=70, y=115)
        f4.pack()
    B4 = Button(f, text = 'Delete a record', command=delrec).place(x=25, y=200)
                                                                
    f.pack()
    
    
def login():
    c='lemon chiffon'
##    img = PhotoImage(file = 'logo.gif')
    f= Frame(win, height=300, width=400, bg=c)
##    pic = Label(f, image=img, height=20, width=20).place(x=5, y=5)
    uname=StringVar()
    pwd=StringVar()

    L = Label(f, text = "Mini Project Hospital", bg = c,
              font = 50).place(x=100, y=10)
    L1 = Label(f, text='Username', bg=c).place(x=75,y=75)
    E1=Entry(f, textvariable=uname).place(x=175,y=75)
    L2 = Label(f, text='Password', bg=c).place(x=75, y=125)
    E2=Entry(f, textvariable=pwd, show='*').place(x=175, y=125)
    
    def clear():
        uname.set('')
        pwd.set('')
        
    def check():
        user = uname.get()
        pswd = pwd.get()
        if user in ['Devanshi', 'Ayushi', 'Muskaan', 'Khushee'] and pswd == 'minipro':
            f.destroy()
            menu()
        else:
            msg=Label(f, text = 'Incorrect Username or Password!!',
                      bg=c, font=70).place(x=60, y=175)
            clear()
        
    clr=Button(f, text='Clear', command=clear).place(x=100, y=225)
    lgn=Button (f,text='Login', command=check).place(x=200, y=225)
    f.pack()

login()

win.mainloop()

from tkinter import *
from sqlconnection_dental import *
from twilio.rest import Client
from tkcalendar import DateEntry,Calendar
B1=""
B2=""
BR=""
name=""
email=""
gender=""
married_status=""
mobile_no=""
whatsapp_no=""
address=""
city=""
age=""
bod=""
schedule_date=""
time=""
password=""
email_sign_in=""
password_sign_in=""
Label20=""
Label21=""



root=Tk()
root.title("Appointment form")
root.geometry("1500x1000")
'''root.configure(bg="teal")'''
root.resizable(0,0)

heading=Label(root,text="Patient Appointment Form",font="arial 15 bold").pack()

def Register():
    Label1=Label(root,text="Enter patient name:")
    Label1.place(x=600,y=30)
    E1=Entry(root)
    E1.place(x=800,y=30)

    Label2 = Label(root, text="Enter Birthdate:")
    Label2.place(x=600,y=60)
    E2 = DateEntry( width= 16,date_pattern="yyyy-mm-dd", background= "magenta3", foreground= "white",bd=2)
    E2.place(x=800,y=60)

    radio = IntVar()
    Label3 = Label(root, text="Gender:")
    Label3.place(x=600,y=90)
    R1 = Radiobutton(root,text="Male", variable=radio, value=1)
    R1.place(x=800,y=90)
    R2 = Radiobutton(root,text="Female", variable=radio, value=2)
    R2.place(x=850,y=90)
    selection=str(radio.get())
    print("Selection"+selection)
    if(selection == 1):
        E3="Male"
    else:
        E3="Female"
    del radio

    r=IntVar()
    Label4 = Label(root, text="Married Status:")
    Label4.place(x=600,y=120)
    R3 = Radiobutton(root, text="Married", variable=r, value=1)
    R3.place(x=800,y=120)
    R4 = Radiobutton(root, text="Unmarried", variable=r, value=2)
    R4.place(x=850,y=120)
    select=str(r.get())
    if(select == 1):
        E4="Married"
    else:
        E4="Unmarried"
    del r

    Label5=Label(root, text="Enter Mobile No:")
    Label5.place(x=600,y=150)
    E5=Entry(root,width=10)
    E5.place(x=800,y=150)

    Label6 = Label(root, text="Enter Whatsapp No:")
    Label6.place(x=600,y=180)
    E6 = Entry(root, width=10)
    E6.place(x=800,y=180)

    Label7=Label(root, text="Enter your Age:")
    Label7.place(x=600,y=210)
    E7=Entry(root)
    E7.place(x=800,y=210)

    Label8=Label(root,text="Enter your Address:")
    Label8.place(x=600,y=240)
    E8=Entry(root)
    E8.place(x=800,y=240)

    Label9 = Label(root, text="City:")
    Label9.place(x=600,y=270)
    E9 = Entry(root)
    E9.place(x=800,y=270)

    Label10 = Label(root, text="Shedule Date:")
    Label10.place(x=600,y=300)
    E10 = DateEntry(width=16,date_pattern="yyyy-mm-dd", background="magenta3", foreground="white", bd=2)
    E10.place(x=800,y=300)


    Label11= Label(root,text="Shedule Time-Slot:")
    Label11.place(x=600,y=330)
    Label12=Label(root,text="(9:00am to 12:00am)")
    Label12.place(x=600,y=350)
    hello = IntVar()
    R5 = Radiobutton(root, text="9:00am", variable=hello, value=1,)
    R5.place(x=800,y=330)
    R6 = Radiobutton(root, text="9:15am", variable=hello, value=2,)
    R6.place(x=900,y=330)
    R7 = Radiobutton(root, text="9:30am", variable=hello, value=3,)
    R7.place(x=1000,y=330)
    R8 = Radiobutton(root, text="9:45am", variable=hello, value=4,)
    R8.place(x=1100,y=330)
    R9 = Radiobutton(root, text="10:00am", variable=hello, value=5,)
    R9.place(x=1200,y=330)
    R10 = Radiobutton(root, text="10:15am", variable=hello, value=6,)
    R10.place(x=800,y=360)
    R11 = Radiobutton(root, text="10:30am", variable=hello, value=7,)
    R11.place(x=900,y=360)
    R12 = Radiobutton(root, text="10:45am", variable=hello, value=8,)
    R12.place(x=1000,y=360)
    R13 = Radiobutton(root, text="11:00am", variable=hello, value=9,)
    R13.place(x=1100,y=360)
    R14 = Radiobutton(root, text="11:15am", variable=hello, value=10,)
    R14.place(x=1200,y=360)
    R15 = Radiobutton(root, text="11:30am", variable=hello, value=11,)
    R15.place(x=800,y=390)
    R16 = Radiobutton(root, text="11:45am", variable=hello, value=12,)
    R16.place(x=900,y=390)
    R17 = Radiobutton(root, text="12:00am", variable=hello, value=13,)
    R17.place(x=1000,y=390)
    sel=str(hello.get())
    print(sel)
    if(sel==1):
        E11="9:00am"
    elif(sel==2):
        E11="9:15am"
    elif (sel == 3):
        E11 = "9:30am"
    elif (sel == 4):
        E11 = "9:45am"
    elif (sel == 5):
        E11 = "10:00am"
    elif (sel == 6):
        E11 = "10:15am"
    elif (sel == 7):
        E11 = "10:30am"
    elif (sel == 8):
        E11 = "10:45am"
    elif (sel == 9):
        E11 = "11:00am"
    elif (sel == 10):
        E11 = "11:15am"
    elif (sel == 11):
        E11 = "11:30am"
    elif (sel == 12):
        E11 = "11:45am"
    else:
        E11 = "12:00am"
    del hello

    def submit():
        name = E1.get()
        bod = E2.get()
        gender = E3
        married_status = E4
        mobile_no=E5.get()
        whatsapp_no = E6.get()
        age=E7.get()
        address= E8.get()
        city= E9.get()
        schedule_date=E10.get()
        time= E11


        print("Entered name is:",name)
        print("Entered birthdate is:", bod)
        print("Entered gender is:", gender)
        print("Entered married status is:", married_status)
        print("Entered mobile number is:", mobile_no)
        print("Entered whatsapp number is:", whatsapp_no)
        print("Entered age is:", age)
        print("Entered address is:", address)
        print("Entered city is:", city)
        print("Entered schedule date is:", schedule_date)
        print("Entered time is:", time)


        mycursor = myDB.cursor()
        sql = "INSERT INTO patient(name,bod,gender,married_status,mobile_no,whatsapp_no,age,address,city,schedule_date,time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value = (name, bod, gender, married_status, mobile_no, whatsapp_no, age, address, city, schedule_date, time)
        mycursor.execute(sql, value)
        myDB.commit()

        Label20=Label(root,text="your appointment schedule successfully!!!!",font="arial 18 bold",fg="green")
        Label20.pack()
        Label21=Label(root, text="Shortly you will receive conformation message from PUSHPAM Dental!!!!", font="arial 18 bold", fg="green")
        Label21.pack()

        def message():
            number="+91"+E5.get()
            client = Client("AC4f4167a70886d42a7cc154f0ce801da3", "5456013fe7de07e975864631d0a24ad4")
            client.messages.create(to=number,
                                   from_="+12176287069",
                                   body="Hello "+E1.get()+", your appointment at PUSHPAM Dental is confirm on date is "+E10.get()+" on time "+E11+".")
        message()

        E1.destroy()
        E2.destroy()
        '''E3.destroy()'''
        '''E4.destroy()'''
        E5.destroy()
        E6.destroy()
        E7.destroy()
        E8.destroy()
        E9.destroy()
        E10.destroy()
        '''E11.destroy()'''
        R1.destroy()
        R2.destroy()
        R3.destroy()
        R4.destroy()
        R5.destroy()
        R6.destroy()
        R7.destroy()
        R8.destroy()
        R9.destroy()
        R10.destroy()
        R11.destroy()
        R12.destroy()
        R13.destroy()
        R14.destroy()
        R15.destroy()
        R16.destroy()
        R17.destroy()

        def remove_text():
            Label1.config(text="")
            Label2.config(text="")
            Label3.config(text="")
            Label4.config(text="")
            Label5.config(text="")
            Label6.config(text="")
            Label7.config(text="")
            Label8.config(text="")
            Label9.config(text="")
            Label10.config(text="")
            Label11.config(text="")
            Label12.config(text="")
            '''L111.config(text="")
            L112.config(text="")
            L113.config(text="")
            L114.config(text="")
            L115.config(text="")
            L116.config(text="")
            L117.config(text="")
            L118.config(text="")
            L119.config(text="")
            L120.config(text="")
            L121.config(text="")
            L122.config(text="")
            L123.config(text="")'''


        remove_text()
        B1.destroy()

    B1=Button(root,text="submit",command=submit)
    B1.place(x=700,y=440)

BR=Button(root,text="Book Appointment",command=Register).place(x=500,y=440)
'''Register();'''

def cancel():
    Label13=Label(root,text="Enter your name:")
    Label13.pack()
    E12=Entry(root)
    E12.pack()
    Label14=Label(root,text="Enter your Mobile number:")
    Label14.pack()
    E13=Entry(root)
    E13.pack()
    def confirm():
        patient_name=E12.get()
        patient_mobile_number=E13.get()
        print("Entered email is:",patient_name)
        print("Entered password is:",patient_mobile_number)

        mycursor = myDB.cursor()
        mycursor.execute("SELECT name,mobile_no FROM patient WHERE name='" + patient_name + "' OR mobile_no= '" + patient_mobile_number + "'")
        myresult=mycursor.fetchone()
        print(myresult)
        database_name=myresult[0]
        print(database_name)
        database_mobile_no=myresult[1]
        print(database_mobile_no)

        if(database_name == patient_name and database_mobile_no == patient_mobile_number  ):
            Label(root,text="Appointment Cancel !!!!",fg="green",font="arial 18 bold").pack()

            def message():
                number = "+91" + E13.get()
                client = Client("AC4f4167a70886d42a7cc154f0ce801da3", "5456013fe7de07e975864631d0a24ad4")
                client.messages.create(to=number,
                                       from_="+12176287069",
                                       body="Hello " + E12.get() + ", your appointment at PUSHPAM Dental is cancel. Visit again !!!.")

            message()

            E12.destroy()
            E13.destroy()
            B2.destroy()
        else:
            Label(root,text="USER DOES NOT EXISTS!!!!",fg="red",font="arial 18 bold").pack()
            E12.destroy()
            E13.destroy()
            B2.destroy()

        def remove_text():
            Label13.config(text="")
            Label14.config(text="")

        remove_text()

    B2=Button(root,text="confirm",command=confirm)
    B2.place(x=850,y=440)
Button(root,text="Cancel",command=cancel).place(x=780,y=440)

root.mainloop()
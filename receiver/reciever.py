from tkinter import *
from network import Sender, Reciever
from tkinter import messagebox, filedialog
import threading
from tkinter.filedialog import asksaveasfilename, askopenfilename

root = Tk()

filename = StringVar()
status = StringVar()
hostinfo = StringVar()
portinfo = IntVar()

hostinfo.set("N/A")
portinfo.set('N/A')
filename.set("N/A")
status.set("N/A")

def exitprog():
    if messagebox.askyesno("Exit Program", "Are you sure you want to exit the program?") == False:
        return False
    exit()

def confirmations(heading, message):
    messagebox.showinfo(heading, message)

def recieve():
    global file_name
    confirmation, file_name = Reciever.recieve(s)
    confirmations("INFO", confirmation)
    filename.set(file_name)

def connect():
    global s
    s = Reciever.connect(host.get(), int(port.get()))
    confirmations("Connected", f"connected to server with connection: {s}")
    status.set("Connected to server")
    hostinfo.set(host.get())
    portinfo.set(port.get())
    thread = threading.Thread(target=recieve)
    thread.start()

frame1 = LabelFrame(root, bg="blue")
frame1.grid(row=0, column=0, padx=10, pady=10)

frame2 = LabelFrame(root, bg="black", borderwidth=3, text="Connection Information")
frame2.grid(row=1, column=0, padx=10, pady=10)

connectbtn = Button(root, text="CONNECT", command=connect, width=20, height=2)
connectbtn.grid(row=2, column=0, padx=30)

frame3 = LabelFrame(root, bg="white", borderwidth=3, text="Transfer Information")
frame3.grid(row=3, column=0)


#FRAME1
title = Label(frame1, text="FILE TRANSIT", font="Arial 30", bg="blue", fg="white", justify="center")
title.pack()


#FRAME2
hostlabel = Label(frame2, text="HOST NAME/IP :", bg="black", fg="WHITE", font="Arial 14")
hostlabel.grid(row=0, column=0)
host = Entry(frame2, width=30, borderwidth=5)
host.grid(row=0, column=1)

portlabel = Label(frame2, text="HOST PORT :", bg="black", fg="white", font="Arial 14")
portlabel.grid(row=1, column=0)
port = Entry(frame2, width=30, borderwidth=5)
port.grid(row=1, column=1)


#FRAME3
hostlabel = Label(frame3, text="HOST :", font="Arial 10", bg="white", fg="black")
hostlabel.grid(row=0, column=0)
portlabel = Label(frame3, text="PORT", bg="white", font="Arial 10", fg="black")
portlabel.grid(row=1, column=0, padx=30)

hostlabeldata = Label(frame3, textvariable=hostinfo, font="Arial 10", bg="white", fg="black")
hostlabeldata.grid(row=0, column=1)
portlabeldata = Label(frame3, textvariable=portinfo, font="Arial 10", bg="white", fg="black")
portlabeldata.grid(row=1, column=1, padx=30)

Connstat = Label(frame3, text="Status :", font="Arial 10", bg="white", fg="black")
Connstat.grid(row=2, column=0)    
Connstatdata = Label(frame3, textvariable=status, font="Arial 10", bg="white", fg="black")
Connstatdata.grid(row=2, column=1)

filenamelbl = Label(frame3, text="File Name", font="Arial 10", bg="white", fg="black")
filenamelbl.grid(row=3, column=0)    
filenamelbldata = Label(frame3, textvariable=filename, font="Arial 10", bg="white", fg="black")
filenamelbldata.grid(row=3, column=1)


# exitbtn = Button(root, text="Cancel", font="ArialBlack 18", bg="red", command=exitprog)
# exitbtn.grid(row=2, column=0)


root.configure(background="red")
root.title("FILE TRANSIT - Reciever")
root.resizable(False, False)
root.mainloop()
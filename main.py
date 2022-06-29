from tkinter import *
from network import Sender
from tkinter import messagebox, filedialog
import threading
from tkinter.filedialog import asksaveasfilename, askopenfilename
import os


cwd = os.getcwd()
root = Tk()
server_status = StringVar()
server_info = StringVar()
clientaddr = StringVar()
filenamevar = StringVar()
# num_clients = IntVar()
filename = StringVar()
filepath = StringVar()
clients = []


clientaddr.set("N/A")
server_info.set("Not Connected")
# num_clients.set(0)
filename.set("N/A")
filenamevar.set("N/A")
filepath.set("N/A")

def exitprog():
    if messagebox.askyesno("Exit Program", "Are you sure you want to exit the program?") == False:
        return False
    exit()

def confirmations(heading, message):
    messagebox.showinfo(heading, message)


def accept_conn():
    global conn, addr
    conn, addr = Sender.accept_connection(s)
    confirmations(f"File Transit", (f"Client with connection address: {conn}{addr} is connected"))
    clientaddr.set(addr)
    server_info.set(f"Connected")
    server_status.set(f"ACTIVE...")

def create_server():
    # global conn, addr
    global host, port, s
    host, port, s = Sender.create_server()
    server_status.set("ACTIVE")
    thread = threading.Thread(target=accept_conn)
    thread.start()
    return host, port#, conn, addr

def send1(filename, filepath):
    for conn in clients:
        try:
            confirmation = Sender.send(filepath, filename, conn)
        except Exception as e:
            pass
        server_status.set(f"{confirmation}")
        confirmations("File Transit", confirmation)




frame1 = LabelFrame(root, bg="black")
frame1.grid(row=0, column=0, padx=10, pady=10)
title = Label(frame1, text="FILE TRANSIT", font="Arial 30", bg="white", fg="blue", justify="center")
title.pack()

frame2 = LabelFrame(root, bg="white", borderwidth=4)
frame2.grid(row=1, column=0, padx=10, pady=10)

host, port= create_server()

hostlabel = Label(frame2, text="HOST :", font="Arial 10", bg="white", fg="black")
hostlabel.grid(row=0, column=0)
portlabel = Label(frame2, text="PORT", bg="white", font="Arial 10", fg="black")
portlabel.grid(row=1, column=0, padx=30)

hostlabeldata = Label(frame2, text=host, font="Arial 10", bg="white", fg="black")
hostlabeldata.grid(row=0, column=1)
portlabeldata = Label(frame2, text=port, font="Arial 10", bg="white", fg="black")
portlabeldata.grid(row=1, column=1, padx=30)

serverinfolbl = Label(frame2, text="Server Information :", font="Arial 10", bg="white", fg="black")
serverinfolbl.grid(row=2, column=0)    
serverinfolabel = Label(frame2, textvariable=server_info, font="Arial 10", bg="white", fg="black")
serverinfolabel.grid(row=2, column=1)

# clientsnumlbl = Label(frame2, text="NO. of clients :", font="Arial 10", bg="white", fg="black")
# clientsnumlbl.grid(row=3, column=0)    
# clientsnumlabel = Label(frame2, textvariable=num_clients, font="Arial 10", bg="white", fg="black")
# clientsnumlabel.grid(row=3, column=1)

clientaddrlbl = Label(frame2, text="Client address :", font="Arial 10", bg="white", fg="black")
clientaddrlbl.grid(row=4, column=0)    
clientaddress = Label(frame2, textvariable=clientaddr, font="Arial 10", bg="white", fg="black")
clientaddress.grid(row=4, column=1)


serverstatuslbl = Label(frame2, text="Server status :", font="Arial 10", bg="white", fg="black")
serverstatuslbl.grid(row=5, column=0)    
serverstatuslabel = Label(frame2, textvariable=server_status, font="Arial 10", bg="white", fg="black")
serverstatuslabel.grid(row=5, column=1)

filenamelbl = Label(frame2, text="File Name :", font="Arial 10", bg="white", fg="black")
filenamelbl.grid(row=6, column=0)    
filenamelbldata = Label(frame2, textvariable=filenamevar, font="Arial 10", bg="white", fg="black")
filenamelbldata.grid(row=6, column=1)

frame3 = LabelFrame(root, bg="white", borderwidth=4)
frame3.grid(row=2, column=0, padx=10, pady=10)

def choose_file():
    global file
    filepath = askopenfilename(initialdir=cwd, title="Choose A file", filetypes=(("All Files", "*.*"), ))
    # print(filepath)
    index = (filepath.rfind("/"))
    filename = filepath[index+1:]
    filenamevar.set(filename)
    send1(filename, filepath)

choosefile = Button(frame3, text="CHOOSE A FILE", command=choose_file)
choosefile.grid(row=0, column=0, padx=30)


root.configure(background="blue")
root.title("FILE TRANSIT")
root.resizable(False, False)


root.mainloop()
import socket
import time
import threading
from tkinter import *

root = Tk()
root.geometry('300x500')
root.config(bg='white')

start_chat_image = PhotoImage(file='start.png')

def func():
    t = threading.Thread(target=recv)
    t.start()

def thread_send_message():
    listen_socket=socket.socket()
    port = 3050
    max_connection=99
    ip=socket.gethostname()
    print(ip)
    

button = Button(root, image=start_chat_image, command=func,borderwidth=0)
button.place(x=90, y=90)

message=StringVar()
message_box=Entry(root, textvariable=message, font=('calbre', 10, 'normal'), border=2, width=32)
message_box.place(x=40,y=444)

send_message_img = PhotoImage(file='send.png')

send_message_button=Button(root, image=start_chat_image, command=func,borderwidth=0)
send_message_button.place(x=90, y=90)

list_box = Listbox(root, height=20, width=43)
listbox.place(x=15, y =80)


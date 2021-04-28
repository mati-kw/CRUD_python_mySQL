import mysql.connector
from mysql.connector import errorcode
import config
import time
import datetime
import tkinter as tk #sudo apt-get install python3-tk



#próba podłączenia sie do bazy doanych
try:
  cnx = mysql.connector.connect(user=config.user, password=config.password,host=config.host,database=config.database)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

cursor = cnx.cursor(buffered=True)

def add_record(first,last):
  name = "'"+ str(first)+ "'"
  surname = "'"+ str(last)+ "'"
  #przerobienie podanych argumentów na string do postaci wyołania stworzonej procedury
  add_guest = ("call add_guest("+name+","+surname+")") 
  print(add_guest)
  cursor.execute(add_guest)
  cnx.commit()


# add_record("Natalia","Bien")

def delete_record(identyficator):
  num = str(identyficator)
  #przerobienie podanych argumentów na string do postaci wyołania stworzonej procedury
  delete_guest = ("call delete_guest("+num+")")
  print(delete_guest)
  cursor.execute(delete_guest)
  cnx.commit()

# delete_record(7)

def update_record(identificator,first,last):
  name = "'"+ str(first)+ "'"
  surname = "'"+ str(last)+ "'"
  num = str(identificator)
  #przerobienie podanych argumentów na string do postaci wyołania stworzonej procedury
  update_guest = ("call update_record("+num+","+name+","+surname+")")
  print(update_guest)
  cursor.execute(update_guest)
  cnx.commit()

# update_record(1,"Kuba","Czerwiec")

def show_all():
  query = ("SELECT * FROM MyGuests")
  cursor.execute(query)
  
  global display_database
  display_database=""

  for (id,firstname, lastname) in cursor:
    display_database +=str( ("{},{},{}\n".format(id,firstname,lastname)))
  cnx.commit()
  return display_database
  
  
# show_all()


root = tk.Tk()

def print_function(bullshit):
    print(bullshit)
    print(type(bullshit))

def refreshDatabase(self):
    self.destroy()
    open_window4()


def open_window():
    new_window = tk.Toplevel(root)
    new_window.title("Add records")
    new_window.geometry("250x250")

    l1 = tk.Label(new_window, text="Name:")
    l1.pack()

    text_entry = tk.Entry(new_window)
    text_entry.pack()

    l2 = tk.Label(new_window, text="Surname:")
    l2.pack()

    text_entry2 = tk.Entry(new_window)
    text_entry2.pack()

    bt1 = tk.Button(new_window, text="Add record", command=lambda: add_record(text_entry.get(),text_entry2.get()))
    bt1.pack(pady=20)
    bt2 = tk.Button(new_window, text="Close", command=new_window.destroy)
    bt2.pack(pady=20)


def open_window2():
    new_window = tk.Toplevel(root)
    new_window.title("Delete records")
    new_window.geometry("250x250")

    l1 = tk.Label(new_window, text="id:")
    l1.pack()

    text_entry = tk.Entry(new_window, width=3, justify="right")
    text_entry.pack()

    bt1 = tk.Button(new_window, text="Delete record", command=lambda: delete_record(text_entry.get()))
    bt1.pack(pady=20)
    bt2 = tk.Button(new_window, text="Close", command=new_window.destroy)
    bt2.pack(pady=20)


def open_window3():
    new_window = tk.Toplevel(root)
    new_window.title("Update records")
    new_window.geometry("250x300")

    l0 = tk.Label(new_window, text="Choose record id")
    l0.pack()

    id_entry = tk.Entry(new_window, width=3, justify="right")
    id_entry.pack()

    l1 = tk.Label(new_window, text="New name:")
    l1.pack()

    text_entry = tk.Entry(new_window)
    text_entry.pack()

    l2 = tk.Label(new_window, text="New surname:")
    l2.pack()

    text_entry2 = tk.Entry(new_window)
    text_entry2.pack()

    bt1 = tk.Button(new_window, text="Update record",
                    command=lambda: update_record(id_entry.get(),text_entry.get(),text_entry2.get()))
    bt1.pack(pady=20)
    bt2 = tk.Button(new_window, text="Close", command=new_window.destroy)
    bt2.pack(pady=20)


def open_window4():
    new_windowR = tk.Toplevel(root)
    new_windowR.title("Test database")
    new_windowR.geometry('%dx%d+%d+%d' % (400, 600, 700, 100))

    bt1 = tk.Button(new_windowR, text="Refresh",command=lambda: refreshDatabase(new_windowR))
    bt1.pack(pady=5)


    some_text = show_all()
    w = tk.Text(new_windowR)
    w.insert("insert", some_text)
    w.pack()


root.title("Simple CRUD App")
root.geometry("450x300")
tk.Label(root, text="App for adding, deleting and modifying records in test database").place(x=5, y=10)

button1 = tk.Button(root, text="Add record", height=1, width=15, command=open_window)
button1.place(x=20, y=60, in_=root)

button1 = tk.Button(root, text="Delete record", height=1, width=15, command=open_window2)
button1.place(x=20, y=100, in_=root)

button1 = tk.Button(root, text="Update record", height=1, width=15, command=open_window3)
button1.place(x=20, y=140, in_=root)

button1 = tk.Button(root, text="Show database", height=1, width=15, command=open_window4)
button1.place(x=20, y=180, in_=root)

root.mainloop()
cursor.close()
cnx.close()


# TESTING PLACE:
# str() 
# first = "'Pyton'"
# last = "'Waz'"
# add_guest = ("call add_guest("+first+","+last+")")
# print(add_guest)
# cursor.execute(add_guest)

# identificator = "6"
# delete_guest = ("call delete_guest("+identificator+")")
# print(delete_guest)
# cursor.execute(delete_guest)

# TIME FORMAT FOR SQL
# today= time.time()
# todaystamp=datetime.datetime.fromtimestamp(today).strftime('%Y-%m-%d %H:%M:%S')
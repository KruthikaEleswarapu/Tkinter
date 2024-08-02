from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title('Using database')
root.geometry("400x400")


def submit():
    #create a database or connect to one
    conn=sqlite3.connect('address_book.db')
    #create a cursor
    c=conn.cursor()
    #insert into table
    c.execute("insert into addresses values(:f_name,:l_name,:address,:state,:city,:zipcode)",{'f_name':f_name.get(),'l_name':l_name.get(),'address':address.get(),'state':state.get(),'city':city.get(),'zipcode':zipcode.get(),})
    #to commit the changes
    conn.commit()
    #to explicitly close connection
    conn.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    state.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)

def query():
    conn=sqlite3.connect('address_book.db')
    #create a cursor
    c=conn.cursor()
    #insert into table
    #oid is primary key
    c.execute("select *,oid from addresses")
    #fetchonr():fetches first record,fetchmany(n): fetches n records,fetchall(): fetches all records
    records=c.fetchall()
    print(records)
    #to commit the changes
    conn.commit()
    #to explicitly close connection
    conn.close()

def delete():
    conn=sqlite3.connect('address_book.db')
    #create a cursor
    c=conn.cursor()
    #insert into table
    #oid is primary key
    c.execute("delete from addresses where oid="+delete_box.get())
    delete_box.delete(0,END)
    #to commit the changes
    conn.commit()
    #to explicitly close connection
    conn.close()

def update():
    conn=sqlite3.connect('address_book.db')
    #create a cursor
    c=conn.cursor()
    #insert into table
    #oid is primary key
    record_id=delete_box.get()
    c.execute("""update addresses set
              first_name= :first,
              last_name=:last,
              address=:address,
              state=:state,
              city=:city,
              zipcode=:zipcode
              where oid=:oid""",
              {'first':f_name.get(),
               'last':l_name.get(),
               'address':address.get(),
               'state':state.get(),
               'city':city.get(),
               'zipcode':zipcode.get(),
               'oid':record_id,
                  
              })
    #to commit the changes
    conn.commit()
    #to explicitly close connection
    conn.close()
    editor.destroy()


def edit():
    global editor
    editor=Tk()
    editor.title('Update database')
    editor.geometry("400x400")
    conn=sqlite3.connect('address_book.db')
    #create a cursor
    c=conn.cursor()
    #insert into table
    #oid is primary key
    record_id=delete_box.get()
    c.execute("select * from addresses where oid="+record_id)
    global f_name
    global l_name
    global address
    global state
    global city
    global zipcode

    f_name=Entry(editor,width=30)
    f_name.grid(row=0,column=1,padx=20)

    l_name=Entry(editor,width=30)
    l_name.grid(row=1,column=1,padx=20)

    address=Entry(editor,width=30)
    address.grid(row=2,column=1,padx=20)

    city=Entry(editor,width=30)
    city.grid(row=3,column=1,padx=20)

    state=Entry(editor,width=30)
    state.grid(row=4,column=1,padx=20)

    zipcode=Entry(editor,width=30)
    zipcode.grid(row=5,column=1,padx=20)

    f_name_label=Label(editor,text="First Name")
    f_name_label.grid(row=0,column=0)

    l_name_label=Label(editor,text="Last Name")
    l_name_label.grid(row=1,column=0)

    address_label=Label(editor,text="Address")
    address_label.grid(row=2,column=0)

    city_label=Label(editor,text="State")
    city_label.grid(row=3,column=0)

    state_label=Label(editor,text="City")
    state_label.grid(row=4,column=0)
  
    zipcode_label=Label(editor,text="Zipcode")
    zipcode_label.grid(row=5,column=0)

    records=c.fetchall()
    for record in records:
        f_name.insert(0,record[0])
        l_name.insert(0,record[1])
        address.insert(0,record[2])
        state.insert(0,record[3])
        city.insert(0,record[4])
        zipcode.insert(0,record[5])
    
    save=Button(editor,text="Save",command=update)
    save.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

    #to commit the changes
    conn.commit()
    #to explicitly close connection
    conn.close()


#since the above and below are in different windows we can use same name for labels
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)

address=Entry(root,width=30)
address.grid(row=2,column=1,padx=20)

city=Entry(root,width=30)
city.grid(row=3,column=1,padx=20)

state=Entry(root,width=30)
state.grid(row=4,column=1,padx=20)

zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)

delete_box=Entry(root,width=30)
delete_box.grid(row=9,column=1,padx=20)


f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0)

l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)

address_label=Label(root,text="Address")
address_label.grid(row=2,column=0)

city_label=Label(root,text="State")
city_label.grid(row=3,column=0)

state_label=Label(root,text="City")
state_label.grid(row=4,column=0)

zipcode_label=Label(root,text="Zipcode")
zipcode_label.grid(row=5,column=0)

delete_box_label=Label(root,text="Select ID")
delete_box_label.grid(row=9,column=0)

submit=Button(root,text="Submit",command=submit)
submit.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#create a query
query=Button(root,text="Show Records",command=query)
query.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

delete=Button(root,text="Delete Record",command=delete)
delete.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

edit=Button(root,text="Edit Record",command=edit)
edit.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=142)

#to create table
'''c.execute("""create table addresses(first_name text,
zipcode integer)
""")
'''

root.mainloop()
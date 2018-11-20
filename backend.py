from tkinter import *
from tkinter import messagebox
import sqlite3

def print_camp(idd,t1,t2,t3,t4,t5,t6):
    conn=sqlite3.connect("refugee.db")
    cur=conn.cursor()
    cur.execute("select cid from camp where cname like ? ",(idd,))
    row1=cur.fetchall()

    if len(row1)==0:
        messagebox.showerror("ERROR", "NO SUCH CAMP FOUND")
        conn.close()
        return
    
    cur.execute("select d.country_name from camp c,country d where c.countryid=d.coid and c.cname like ? ",(idd,))
    row2=cur.fetchall()
    cur.execute("select total_refugees from camp where cname like ? ",(idd,))
    row3=cur.fetchall()
    cur.execute("select contact from camp where cname like ? ",(idd,))
    row4=cur.fetchall()
    cur.execute("select d.oname from camp c,organization d where c.orgid=d.oid and c.cname like ? ",(idd,))
    row5=cur.fetchall()
    t1.insert(END,row1)
    t2.insert(END,idd)
    t3.insert(END,row2)
    t4.insert(END,row3)
    t5.insert(END,row4)
    t6.insert(END,row5)
    conn.close()

def print_organization(idd,t1,t2,t3,t4,t5,t6):
    conn=sqlite3.connect("refugee.db")
    cur=conn.cursor()
    cur.execute("select oid from organization where oname like ?",(idd,))
    row1=cur.fetchall()

    if len(row1)==0:
        messagebox.showerror("ERROR", "NO SUCH ORGANIZATION FOUND")
        conn.close()
        return
    
    cur.execute("select ovolunteer from organization where oname like ?",(idd,))
    row2=cur.fetchall()
    cur.execute("select ohead from organization where oname like ?",(idd,))
    row3=cur.fetchall()
    cur.execute("select ocountry from organization where oname like ?",(idd,))
    row4=cur.fetchall()
    cur.execute("select ocontact from organization where oname like ?",(idd,))
    row5=cur.fetchall()
    t1.insert(END,row1)
    t2.insert(END,idd)
    t3.insert(END,row3[0][0])
    t4.insert(END,row2)
    t5.insert(END,row4[0][0])
    t6.insert(END,row5)
    conn.close()

def print_person(idd,t1,t2,t3,t4,t5,t6):
    conn=sqlite3.connect("refugee.db")
    cur=conn.cursor()
    cur.execute("select rid from refugee_info where rname=?",(idd,))
    row1=cur.fetchall()

    if len(row1)==0:
        messagebox.showerror("ERROR", "NO SUCH PERSON FOUND")
        conn.close()
        return
    
    cur.execute("select rage from refugee_info where rname like ?",(idd,))
    row2=cur.fetchall()
    cur.execute("select rsex from refugee_info where rname like ?",(idd,))
    row3=cur.fetchall()
    print(row3[0][0])
    if row3[0][0]=="F":
        row3="Female"
    else:
        row3="Male"
    cur.execute("select c.cname from refugee_info r,camp c where c.cid=r.campid and rname=?",(idd,))
    row4=cur.fetchall()
    cur.execute("select base from refugee_info where rname=?",(idd,))
    row5=cur.fetchall()
    t1.insert(END,row1)
    t2.insert(END,idd)
    t3.insert(END,row2)
    t4.insert(END,row3)
    t5.insert(END,row4[0][0])
    t6.insert(END,row5)
    conn.close()

def donate_amount(val1,val2):
    
    conn=sqlite3.connect("refugee.db")
    cur=conn.cursor()
    val2=int(val2)
    cur.execute("select oid from organization where oname like ?",(val1,))
    val1=cur.fetchall()
    if len(val1)==0:
        messagebox.showerror("ERROR", "ENTER A VALID ORGANIZATION NAME")
        conn.close()
        return
    else:
        val1=int(val1[0][0])
        
    cur.execute("insert into Donation_info(amount,orgid) values(?,?)",(val2,val1))
    val2=cur.fetchall()
    conn.commit()
    conn.close()

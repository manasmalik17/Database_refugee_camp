from tkinter import *
#from PIL import ImageTk,Image
import backend


class refugee:

    #functions for calling backend

    def camp_info(self,e1,t1,t2,t3,t4,t5,t6):
        #print(type(e1.get()))
        t1.delete(1.0,END)
        t2.delete(1.0,END)
        t3.delete(1.0,END)
        t4.delete(1.0,END)
        t5.delete(1.0,END)
        t6.delete(1.0,END)
        backend.print_camp(e1.get(),t1,t2,t3,t4,t5,t6)

    def organization_info(self,e1,t1,t2,t3,t4,t5,t6):
        t1.delete(1.0,END)
        t2.delete(1.0,END)
        t3.delete(1.0,END)
        t4.delete(1.0,END)
        t5.delete(1.0,END)
        t6.delete(1.0,END)        
        backend.print_organization(e1.get(),t1,t2,t3,t4,t5,t6)

    def person_info(self,e1,t1,t2,t3,t4,t5,t6):
        t1.delete(1.0,END)
        t2.delete(1.0,END)
        t3.delete(1.0,END)
        t4.delete(1.0,END)
        t5.delete(1.0,END)
        t6.delete(1.0,END)
        backend.print_person(e1.get(),t1,t2,t3,t4,t5,t6)

    def donate(self,e1,e2):
        backend.donate_amount(e1.get(),e2.get())
    
    
    def start_page(self):

        main=Tk()
        main.title("Refugee Aider")
        main.resizable(0,0)
        main.configure(bg='#40caee')  
        #root = Tk()  
        #canvas = Canvas(root, width = 30, height = 30)  
        #canvas.pack()  
        #img = ImageTk.PhotoImage(Image.open("humanity.png"))  
        #canvas.create_image(20, 20, anchor=NW, image=img)  
        #root.mainloop()  
        #main.minsize(width=666, height=666)
        #main.maxsize(width=666, height=666)
        
        #top label:

        Label(main,text="\tWELCOME TO REFUGEE AIDER\t\n",bg="#196aff",fg="#f7f9f9",font=("Roboto",26,"bold bold")).grid(row=0,column=0,sticky=S,columnspan=2)
        #l.config(borderwidth=3)
        #space between buttons
        Label(main,text="\n",bg='#40caee').grid(row=1,column=0,sticky=S)
        
        #button for camp information
        b1=Button(main,text='CAMP INFO',width=30,height=3,bg='#626262',fg="#f7f9f9",font="Arial 17 italic",command=lambda:[main.destroy(),self.camp_page()],cursor="hand2",borderwidth=5, relief = RAISED)
        #b1.configure(command=self.camp_window)
        b1.grid(row=2,column=0,sticky=S,columnspan=2)

        #space between buttons
        Label(main,text="\n",bg='#40caee').grid(row=3,column=0,sticky=S)

        #button for organization information
        b2=Button(main,text='ORGANIZATION INFO',width=30,height=3,bg='#626262',fg="#f7f9f9",font="Arial 17 italic",command=lambda:[main.destroy(),self.organization_page()],cursor="hand2",borderwidth=5)
        b2.grid(row=4,column=0,sticky=S,columnspan=2)

        #space between buttons
        Label(main,text="\n",bg='#40caee').grid(row=5,column=0,sticky=S)

        #button for person information
        b3=Button(main,text='PERSON INFO',width=30,height=3,bg='#626262',fg="#f7f9f9",font="Arial 17 italic",command=lambda:[main.destroy(),self.person_page()],cursor="hand2",borderwidth=5)
        b3.grid(row=6,column=0,sticky=S,columnspan=2)

        #space between buttons
        Label(main,text="\n",bg='#40caee').grid(row=7,column=0,sticky=S)

        #button for making donation
        b4=Button(main,text='CONTRIBUTE',width=30,height=3,bg='#626262',fg="#f7f9f9",font="Arial 17 italic",command=lambda:[main.destroy(),self.donate_page()],cursor="hand2",borderwidth=5)
        b4.grid(row=8,column=0,sticky=S,columnspan=2)

        #space between buttons
        Label(main,text="\n\n",bg='#40caee').grid(row=9,column=0,sticky=S)

        b3=Button(main,text='Quit',width=15,height=2,bg='#686868',fg="#f7f9f9",font='Arial 8',command=lambda: exit(),cursor="hand2")
        b3.grid(row=9,column=1,sticky=E)

        main.mainloop()

    def camp_page(self):
        camp=Tk()
        camp.configure(bg="#196aff")
        camp.resizable(0,0)
        #generic header
        Label(camp,text="Welcome to Refugee Aider\n",bg="#196aff",fg="#f7f9f9",font=("courier new",24,"italic bold")).grid(row=0,column=0,sticky=S,columnspan=3)

        #camp specific label
        Label(camp,text="CAMP INFORMATION CENTRE\n",bg="#196aff",fg="#f7f9f9",font=("courier new",20,"italic bold")).grid(row=1,column=0,sticky=S,columnspan=3)

        #query label
        Label(camp,text="Enter Camp Name:\n\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",16,"italic bold")).grid(row=2,column=0,sticky=S,columnspan=3)

        #entry box
        e1=Entry(camp,width=50,bg="white")
        e1.grid(row=3,column=0,sticky=S,columnspan=3)
        e1.focus()

        #submission button
        b2=Button(camp,text='SEARCH',width=6,bg='#330066',fg="#f7f9f9",font="Arial 10 bold",command=lambda:self.camp_info(e1,t1,t2,t3,t4,t5,t6))
        b2.grid(row=4,column=0,sticky=S,columnspan=3)

        #space between buttons
        Label(camp,text="\n",bg='#196aff').grid(row=5,column=0,sticky=S)

        #information labels and text boxes
        l1=Label(camp,text="Camp ID :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"bold"))
        t1=Text(camp,width=40,height=2,bg='white',wrap=WORD)
        l2=Label(camp,text="\nName    :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"bold"))
        t2=Text(camp,width=40,height=2,bg='white',wrap=WORD)
        l3=Label(camp,text="\nCountry :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"bold"))
        t3=Text(camp,width=40,height=2,bg='white',wrap=WORD)
        l4=Label(camp,text="\nNumber of Inhabitants :\n",bg="#2159a8",fg="white",font=("courier new",12,"bold"))
        t4=Text(camp,width=40,height=2,bg='white',wrap=WORD)
        l5=Label(camp,text="\nOfficial Contact :\n",bg="#2159a8",fg="white",font=("courier new",12,"bold"))
        t5=Text(camp,width=40,height=2,bg='white',wrap=WORD)
        l6=Label(camp,text="\nHead Organization :\n",bg="#2159a8",fg="white",font=("courier new",12,"bold"))
        t6=Text(camp,width=40,height=2,bg='white',wrap=WORD)

        l1.grid(row=6,column=0,sticky=W)
        t1.grid(row=7,column=0,sticky=W)
        l2.grid(row=6,column=2,sticky=W)
        t2.grid(row=7,column=2,sticky=W)
        l3.grid(row=8,column=0,sticky=W)
        t3.grid(row=9,column=0,sticky=W)
        l4.grid(row=8,column=2,sticky=W)
        t4.grid(row=9,column=2,sticky=W)
        l5.grid(row=10,column=0,sticky=W)
        t5.grid(row=11,column=0,sticky=W)
        l6.grid(row=10,column=2,sticky=W)
        t6.grid(row=11,column=2,sticky=W)
        
        #space between buttons
        Label(camp,text="\n",bg='#196aff').grid(row=12,column=0,sticky=S)
        Label(camp,text="\t    ",bg='#196aff').grid(row=13,column=1,sticky=W)
        b3=Button(camp,text='Quit',width=15,height=2,bg='#626262',fg="#f7f9f9",font='Arial 8',command=lambda: exit())
        b3.grid(row=13,column=2,sticky=E)

        b1=Button(camp,text='Back to\nMain Menu',width=15,height=2,bg='#626262',fg="#f7f9f9",font="Arial 8",command=lambda:[camp.destroy(),self.start_page()])
        b1.grid(row=14,column=2,sticky=E)
        
        camp.mainloop()
        
    def organization_page(self):
        org=Tk()
        org.configure(bg="#196aff")
        org.resizable(0,0)
        #generic header
        Label(org,text="WELCOME TO REFUGEE AIDER\n",bg="#196aff",fg="#f7f9f9",font=("courier new",24,"italic bold")).grid(row=0,column=0,sticky=S,columnspan=3)

        #org specific label
        Label(org,text="ORGANIZATION INFORMATION CENTRE\n",bg="#196aff",fg="#f7f9f9",font=("courier new",20,"italic bold")).grid(row=1,column=0,sticky=S,columnspan=3)

        #query label
        Label(org,text="Enter Organization Name:\n\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",16,"italic bold")).grid(row=2,column=0,sticky=S,columnspan=3)

        #entry box
        e1=Entry(org,width=50,bg="white")
        e1.grid(row=3,column=0,sticky=S,columnspan=3)
        e1.focus()

        #submission button
        b2=Button(org,text='SEARCH',width=6,bg='#330066',fg="#f7f9f9",font="Arial 10 bold",command=lambda:self.organization_info(e1,t1,t2,t3,t4,t5,t6))
        b2.grid(row=4,column=0,sticky=S,columnspan=3)

        #space between buttons
        Label(org,text="\n",bg='#196aff').grid(row=5,column=0,sticky=S)

        #information labels and text boxes
        l1=Label(org,text="Organization ID :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"italic bold"))
        t1=Text(org,width=40,height=2,bg='white',wrap=WORD)
        l2=Label(org,text="\nName    :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"italic bold"))
        t2=Text(org,width=40,height=2,bg='white',wrap=WORD)
        l3=Label(org,text="\nHead :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"italic bold"))
        t3=Text(org,width=40,height=2,bg='white',wrap=WORD)
        l4=Label(org,text="\nVolunteers :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"italic bold"))
        t4=Text(org,width=40,height=2,bg='white',wrap=WORD)
        l5=Label(org,text="\nBase Country :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"italic bold"))
        t5=Text(org,width=40,height=2,bg='white',wrap=WORD)
        l6=Label(org,text="\nOfficial Contact :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"italic bold"))
        t6=Text(org,width=40,height=2,bg='white',wrap=WORD)
        l1.grid(row=6,column=0,sticky=W)
        t1.grid(row=7,column=0,sticky=W)
        l2.grid(row=6,column=2,sticky=W)
        t2.grid(row=7,column=2,sticky=W)
        l3.grid(row=8,column=0,sticky=W)
        t3.grid(row=9,column=0,sticky=W)
        l4.grid(row=8,column=2,sticky=W)
        t4.grid(row=9,column=2,sticky=W)
        l5.grid(row=10,column=0,sticky=W)
        t5.grid(row=11,column=0,sticky=W)
        l6.grid(row=10,column=2,sticky=W)
        t6.grid(row=11,column=2,sticky=W)


        #space between buttons
        Label(org,text="\n",bg='#196aff').grid(row=12,column=0,sticky=S)
        Label(org,text="\t    ",bg='#196aff').grid(row=13,column=1,sticky=W)

        b3=Button(org,text='Quit',width=15,height=2,bg='#626262',fg="#f7f9f9",font='Arial 8',command=lambda: exit())
        b3.grid(row=13,column=2,sticky=E)

        b1=Button(org,text='Back to\nMain Menu',width=15,height=2,bg='#626262',fg="#f7f9f9",font="Arial 8",command=lambda:[org.destroy(),self.start_page()])
        b1.grid(row=14,column=2,sticky=E)
                
        org.mainloop()

##person information page

    def person_page(self):
        ##    person=Tk()
        ##    person.configure(bg="#626262")
        ##    person.resizable(0,0)
        ##    #generic header
        ##    Label(person,text="    Welcome to Refugee Aider..\n",bg="#626262",fg="black",font=("courier new",24,"italic bold")).grid(row=0,column=0,sticky=S)
        ##
        ##    #person specific label
        ##    Label(person,text="    PERSON INFORMATION CENTRE\n",bg="#626262",fg="black",font=("courier new",20,"italic bold")).grid(row=1,column=0,sticky=S)
        ##
        ##    #query label
        ##    Label(person,text="    Enter Name of Person:\n",bg="#626262",fg="black",font=("courier new",16)).grid(row=2,column=0,sticky=S)

        person=Tk()
        person.configure(bg="#196aff")
        person.resizable(0,0)
        #generic header
        Label(person,text="WELCOME TO REFUGEE AIDER\n",bg="#196aff",fg="#f7f9f9",font=("courier new",24,"italic bold")).grid(row=0,column=0,sticky=S,columnspan=3)

        #org specific label
        Label(person,text="PERSON INFORMATION CENTRE\n",bg="#196aff",fg="#f7f9f9",font=("courier new",20,"italic bold")).grid(row=1,column=0,sticky=S,columnspan=3)

        #query label
        Label(person,text="Enter Name of Person:\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",16,"italic bold")).grid(row=2,column=0,sticky=S,columnspan=3)


        #entry box
        e1=Entry(person,width=50,bg="white")
        e1.grid(row=3,column=0,sticky=S,columnspan=3)
        e1.focus()


        #submission button
        b2=Button(person,text='SEARCH',width=6,bg='#330066',fg="#f7f9f9",font="Arial 10 bold",command=lambda: self.person_info(e1,t1,t2,t3,t4,t5,t6))
        b2.grid(row=4,column=0,sticky=S,columnspan=3)

        #space between buttons
        Label(person,text="\n",bg='#196aff').grid(row=5,column=0,sticky=S)

        #information labels and text boxes
        l1=Label(person,text="Person ID :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"italic bold"))
        t1=Text(person,width=40,height=2,bg='white',wrap=WORD)
        l2=Label(person,text="\nName    :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"italic bold"))
        t2=Text(person,width=40,height=2,bg='white',wrap=WORD)
        l3=Label(person,text="\nAge :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"italic bold"))
        t3=Text(person,width=40,height=2,bg='white',wrap=WORD)
        l4=Label(person,text="\nSex :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"italic bold"))
        t4=Text(person,width=40,height=2,bg='white',wrap=WORD)
        l5=Label(person,text="\nResiding Camp :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"italic bold"))
        t5=Text(person,width=40,height=2,bg='white',wrap=WORD)
        l6=Label(person,text="\nHome Country :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",12,"italic bold"))
        t6=Text(person,width=40,height=2,bg='white',wrap=WORD)
        l1.grid(row=6,column=0,sticky=W)
        t1.grid(row=7,column=0,sticky=W)
        l2.grid(row=6,column=2,sticky=W)
        t2.grid(row=7,column=2,sticky=W)
        l3.grid(row=8,column=0,sticky=W)
        t3.grid(row=9,column=0,sticky=W)
        l4.grid(row=8,column=2,sticky=W)
        t4.grid(row=9,column=2,sticky=W)
        l5.grid(row=10,column=0,sticky=W)
        t5.grid(row=11,column=0,sticky=W)
        l6.grid(row=10,column=2,sticky=W)
        t6.grid(row=11,column=2,sticky=W)


        #space between buttons
        Label(person,text="\n",bg='#196aff').grid(row=12,column=0,sticky=S)
        Label(person,text="\t    ",bg='#196aff').grid(row=13,column=1,sticky=W)

        b3=Button(person,text='Quit',width=15,height=2,bg='#626262',fg="#f7f9f9",font='Arial 8',command=lambda: exit())
        b3.grid(row=14,column=2,sticky=E)

        b1=Button(person,text='Back to\nMain Menu',width=15,height=2,bg='#626262',fg="#f7f9f9",font="Arial 8",command=lambda:[person.destroy(),self.start_page()])
        b1.grid(row=15,column=2,sticky=E)
                
        person.mainloop()

    def donate_page(self):
        donate=Tk()
        donate.configure(bg="#196aff")
        donate.resizable(0,0)
        #generic header
        Label(donate,text="\tWELCOME TO REFUGEE AIDER\t\n",bg="#196aff",fg="#f7f9f9",font=("courier new",24,"italic bold")).grid(row=0,column=0,sticky=S,columnspan=2)

        #org specific label
        Label(donate,text="DONATION CENTRE\n",bg="#196aff",fg="#f7f9f9",font=("courier new",20,"italic bold")).grid(row=1,column=0,sticky=S,columnspan=2)

        #query label
        Label(donate,text="Enter Name of Organization :\n",bg="#2159a8",fg="#f7f9f9",font=("courier new",16,"italic bold")).grid(row=2,column=0,sticky=S,columnspan=2)


        #entry box 1
        e1=Entry(donate,width=50,bg="white")
        e1.grid(row=3,column=0,sticky=S,columnspan=2)
        e1.focus()

        #space between buttons
        Label(donate,text="\n",bg='#196aff').grid(row=4,column=0,sticky=S)

        #query label
        Label(donate,text="Donation Amount :\n",bg="#2159a8",fg="white",font=("courier new",16,"italic bold")).grid(row=5,column=0,sticky=S,columnspan=2)

        #entry box 2
        e2=Entry(donate,width=50,bg="white")
        e2.grid(row=6,column=0,sticky=S,columnspan=2)
        e2.focus()

        #donate button
        b2=Button(donate,text='DONATE',width=6,bg='#2159a8',fg="#f7f9f9",font="Helvetica",command=lambda:self.donate(e1,e2))
        b2.grid(row=7,column=0,sticky=S,columnspan=2)

        #space between buttons
        Label(donate,text="\n",bg='#196aff').grid(row=8,column=0,sticky=S)

        #textbox
        t1=Text(donate,width=96,height=13,bg='#196aff',fg='#f7f9f9',font=("courier new",10,"italic bold"),wrap=WORD,borderwidth=0)
        t1.grid(row=9,column=0,sticky=S,columnspan=2)
        t1.insert(END,"One book, one pen, one child, and one teacher can change the world.-- Malala Yousafzai \n\nWhen hearing of refugee camps, whether in conversations or in media, we tend to think of a passive group of individuals almost entirely dependent on the outside for any form of assistance.\nWe naturally sympathise with the many who endure sometime unimaginable hardship while hoping for a better future.However a closer look into refugee camps reveals a potentially unexpected and even fascinating inner life from which we on the outside could and perhaps should learn.")

        Label(donate,text="\n",bg='#196aff').grid(row=10,column=0,sticky=S)
        
        b3=Button(donate,text='Quit',width=15,height=2,bg='#626262',fg="#f7f9f9",font='Helvetica',command=lambda: exit())
        b3.grid(row=11,column=1,sticky=E)
        
        b1=Button(donate,text='Back to\nMain Menu',width=15,height=2,bg='#626262',fg="#f7f9f9",font="Helvetica",command=lambda:[donate.destroy(),self.start_page()])
        b1.grid(row=12,column=1,sticky=E)


        donate.mainloop()


        
        


r=refugee()
#r.organization_page()
r.start_page()
#r.camp_page()

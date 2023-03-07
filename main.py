from tkinter import *
import json
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import secrets 
def random_password():
    length=20
    s=[]
    psw_characters=[]
    for i in range(length):
        s.append(secrets.choice(range(33,126))) 
    for i in s:
        psw_characters.append(chr(i))
    password=''.join(psw_characters)

    entry_password.insert(END,string=f"{password}")
    return password
   

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website=entry_website.get()
    emailusr=entry_email.get()
    password_generated=entry_password.get()
    new_data={website:{ "email":emailusr,"password":password_generated}}

    if len(website)==0 or len(password_generated)==0:
        messagebox.showinfo(title="Sorry", message="Please make sure you have filled in all the fields")
    else :   
                
        try:
            with open("database.json","r") as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            with open("database.json","w") as data_file:
                # write a new file if not found
                json.dump(new_data, data_file,indent=4)
        else:
            data.update(new_data)
            with open("database.json","w") as data_file:
                json.dump(data, data_file,indent=4)
        finally:
            entry_website.delete(0,END)
            entry_password.delete(0,END)

def search_json():
    website=entry_website.get()
    try: 
        with open("database.json","r") as data_file:
            data=json.load(data_file)
            


    except FileNotFoundError:
        messagebox.showinfo(title=f"{website}", message="No Data File Found")

    else:    
        if website in data:
            email_found=data[website]["email"]
            password_found=data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"email : {email_found} \n password : {password_found}")
        else: 
            messagebox.showinfo(title=f"{website}", message="No details for the website exists")
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(bg="white",padx=30,pady=30)

#Canvas

canvas=Canvas(width=200,height=200,background="white")
mondrian_image=PhotoImage(file="pngegg.png")
canvas.create_image(100,100,image=mondrian_image)
#timer_text=canvas.create_text(103,112,text="00:00", fill="white", font=(FONT_NAME,50))
canvas.grid(row=0,column=0,columnspan=3)


#Labels

email_label=Label(text="Email/Username:",fg="black",bg="white")
email_label.grid(column=0,row=2)

website_label=Label(text="Website:",fg="black",bg="white")
website_label.grid(column=0,row=1)

Password_label=Label(text="Password:",fg="black",bg="white")
Password_label.grid(column=0,row=3)

#Entries

entry_website = Entry()
#Add some text to begin with
#entry.insert(END, string="Some text to begin with.")
#Gets text in entry
#print(entry.get())
entry_website.grid(column=1,row=1,columnspan=1,sticky=E+W)

entry_email=Entry()
entry_email.grid(column=1,row=2,columnspan=2,sticky=E+W)

entry_password=Entry(width=21)
entry_password.grid(column=1,row=3,sticky=E+W)

#Buttons
button_add=Button(text="Add",highlightthickness=0,bg="white",command=save_password)
button_add.grid(column=1,row=4,columnspan=2,sticky=E+W)

button_generate_psw=Button(text="Generate Password",highlightthickness=0,bg="white",command=random_password)
button_generate_psw.grid(column=2,row=3)

button_search=Button(text="Search",highlightthickness=0,bg="white",command=search_json)
button_search.grid(column=2,row=1,sticky=E+W)

window.mainloop()

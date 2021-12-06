from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import csv

# --------------------- GENERATE PASSWORD ----------------------- #
def generate_password():
  password_entry.delete(0, END)
  letters = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  numbers = ['0','1','2','3','4','5','6','7','8','9']
  symbols = ['!','§','$','%','&','/','(',')','=','?','*','+','#']

  password_capital_letters = [choice(capital_letters) for _ in range (randint(2,4))]
  password_letters = [choice(letters) for _ in range (randint(2,4))]
  password_symbols = [choice(symbols) for _ in range (randint(2,4))]
  password_numbers = [choice(numbers) for _ in range (randint(2,4))]

  password_list = password_capital_letters + password_letters + password_symbols + password_numbers

  shuffle(password_list)

  password = "".join(password_list)
  password_entry.insert(0, password)
# --------------------- SAVE PASSWORD ----------------------- #
def save():
  website = website_entry.get()
  password = password_entry.get()

  def question1():
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n "f"\nPassword: {password} \nAre you sure want to save it?")
    if is_ok:
        with open("password_list.csv", "a",newline='') as data_file:
            data_file.write(f"{website},{password}")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

  # read csv to dict
  import csv
  with open("password_list.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',', quotechar = '|')
    counter = 0
    lines = list(reader)
    #print(lines)

    # for row in reader:
    #   if counter != 0:
    #     website_exist = row[0]
    #     password_exist = row[1]
    #   counter += 1

  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title = "Error", message = "Please make sure you haven't left any fields empty.")
  else:
    if len(lines)==0:
      question1()
    else:
      exist=False
      a=[]
      for i in range(0, len(lines)):
        if website == lines[i][0]:
            exist=True
            a.append(i)
      if exist:
          is_ok = messagebox.askokcancel(title=website, message=f"The password for this website already exists: \n "f"\nWebsite: {website} \nAre you sure want to overwrite it?")
          if is_ok:
              for i in range(0, len(a)):
                  lines[a[i]][1] = password
                    # overwriting csv with new password 
                  with open("password_list.csv", "w",newline='') as data_file:
                      writer = csv.writer(data_file)
                      writer.writerows(lines)
                      website_entry.delete(0, END)
                      password_entry.delete(0, END)
          else:
              question1()
      else:
          question1()
# --------------------- UI SETUP ----------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
password_label = Label(text="Password:")
password_label.grid(row=2, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
password_entry = Entry(width=19)
password_entry.grid(row=2, column=1)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=2, column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=3, column=1, columnspan=2)

window.mainloop()
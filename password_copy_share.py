#%%
import pyperclip
import csv

# --------------------- CONVERT LIST TO DICT ----------------------- #
web_liste = []
password_liste = []

with open("password_list.csv", newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter= ',', quotechar = '|')
  counter = 0
  for row in reader:
    if counter != 0:
      website_name = row[0]
      password = row[1]
      web_liste.append(website_name)
      password_liste.append(password)
    counter += 1
    password_dict = dict(zip(web_liste, password_liste))


# ------------------ COPYING PASSWORD -------------------- #
repeat = True

def get_password():
  for site in password_dict:
    print("-" + site)

  try:
    site_selected = input("Which site do you want to choose? ").lower()
    password_selected = password_dict[site_selected]
    pyperclip.copy(password_selected)
    print("-------------------------------------")
    print("Password for", site_selected, "has been copied to clipboard")
  except:
    print("Please choose the site from the list!")
    get_password()

get_password()

while repeat:
  another_password = input("Do you need another password? y/n? ")
  if another_password == "y":
    get_password()
  else:
    print("Goodbye, see you next time!")
    break

# def generate_password():
#   password_entry.delete(0, END)
#   letters = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#   capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#   numbers = ['0','1','2','3','4','5','6','7','8','9']

#   symbols = ['!','§','$','%','&','/','(',')','=','?','*','+','#']

#   password_capital_letters = [choice(capital_letters) for _ in range (randint(2,4))]
#   password_letters = [choice(letters) for _ in range (randint(2,4))]
#   password_symbols = [choice(symbols) for _ in range (randint(2,4))]
#   password_numbers = [choice(numbers) for _ in range (randint(2,4))]

#   password_list = password_capital_letters + password_letters + password_symbols + password_numbers

#   shuffle(password_list)

#   password = "".join(password_list)
  

# def change_password():
#   for site in password_dict:
#     print("-" + site)
#   try:
#     site_change = input("Which site do you want to change? ").lower()
#     password_to_change = password_dict[site_change] 
#     new_password = 
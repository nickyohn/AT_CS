user_data = {"nickyohn": "121702", "jakeyohn": "090705"} 
logged_in = False

class User:
  def __init__(self):
    pass
  
  def check_login(self, username, password):
    if hash(user_data[username]) == password:
      global logged_in
      logged_in = True
      print("\nLogin Successful!\n")
    else:
      print("Username and password do not match. Try again.")	
      logged_in = False

def login(u):
    global username
    username = input('Enter username: ')
    password = hash(input('Enter password: '))
    u.check_login(username, password)

def menu():
  print('Menu Choices')
  print('1: Send a message')
  print('2: Display messages') 
  print('3: Log out')
  choice = input('What would you like to do?') 
  
  if choice == '1':   # send a message
    print('\nSend message')
    recipient = input('\nEnter recipient: ')
    text = input('Enter message: ')
    global message_data
    message_data = {recipient: text}
    print("\nRecipient:", recipient, "\nMessage:", message_data[recipient])
  
  elif choice == '2':   # display a message 
    print('\nDisplay messages\n')
    recipient = username
    print("Message:",message_data[recipient])
    
  elif choice == '3':   # log out 
    print('\nLog out')
    global logged_in
    logged_in = False
  
  else:
    print('please enter a valid choice')
  print()

def main():
    global loggedin
    user = User()
    print('Welcome to ....')
    print()
    while True:
        if logged_in == True: 
            menu()
        else:
            login(user)

main()


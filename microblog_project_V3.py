import shelve
import sys
logged_in = False

def create_account():
  global username
  username = input('Create a username: ')
  password = input('Create a password: ')
  global user_data
  user_data = {username: password}
create_account()

class User:
  def __init__(self):
    pass
  
  def check_login(self, user_name, pass_word):
    for key in user_data:
      if key == user_name:
        print(user_data)
        if hash(user_data[key]) == pass_word:
          global logged_in
          logged_in = True
          print("\nLogin Successful!\n")
        else:
          print("\nUsername and password do not match. Try again.")	
          logged_in = False
      
def login(u):
    user_name = input('\nEnter username: ')
    pass_word = hash(input('Enter password: '))
    u.check_login(user_name, pass_word)

def menu():
  print('Menu Choices:')
  print('1: Send a message')
  print('2: Display messages') 
  print('3: Log out')
  print('4: Quit')
  print('-------------------------')
  choice = input('What would you like to do?') 
 
  if choice == '1':   
    global send
    def send():   # send a message
      print('Send message')
      recipient = input('\nEnter recipient: ')
      text = input('Enter message: ')
      global recipient_data
      recipient_data = {recipient: text}
      global sender_data
      sender_data = {username: text}
      print("\nRecipient:", recipient, "\nMessage:", recipient_data[recipient])
    send()

  elif choice == '2':    
    def display():  # display a message
      print('Display messages\n')
      recipient = username
      for key in sender_data:
        print(key,"says:",recipient_data[recipient])
      def react():  # react to message
        if input("\nWould you like to respond? (yes/no)") == "yes":
          send()
      react()
    display()
        
  elif choice == '3':   # log out 
    def log_out():
      user = User()
      print('Log out')
      global logged_in
      logged_in = False
      if input('\nWould you like to create an account? (yes/no)\n') == 'yes':
        print()
        create_account()
      login(user)
    log_out()

  elif choice == '4':   # quit program 
    save_data()
    sys.exit()
  
  else:
    print('please enter a valid choice')
  print()

# save data using shelves
def save_data():  
  with shelve.open('database') as db:
    db['users'] = user_data
    db['recipient_messages'] = recipient_data
    db['sender_messages'] = sender_data
    for key in db:
      print(key, db[key])


def main():
  global loggedin
  user = User()
  while True:
    if logged_in == True: 
      print('-------------------------')
      print('Welcome to the PACKER DMs.\n')
      menu()
    else:
      login(user)  
    
main()
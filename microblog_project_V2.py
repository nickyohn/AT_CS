import shelve
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
  
  def check_login(self, username, pass_word):
    if hash(user_data[username]) == pass_word:
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
  print('Menu Choices')
  print('1: Send a message')
  print('2: Display messages') 
  print('3: Log out')
  choice = input('\nWhat would you like to do?') 
 
  if choice == '1':   
    global send
    def send():   # send a message
      print('\nSend message')
      recipient = input('\nEnter recipient: ')
      text = input('Enter message: ')
      global message_data
      message_data = {recipient: text}
      print("\nRecipient:", recipient, "\nMessage:", message_data[recipient])
    send()

  elif choice == '2':    
    def display():  # display a message
      print('\nDisplay messages\n')
      recipient = username
      print("Message:",message_data[recipient])
      def react():  # react to message
        if input("\nWould you like to respond? (yes/no)") == "yes":
          send()
      react()
    display()
        
  elif choice == '3':   # log out 
    def log_out():
      print('\nLog out')
      global logged_in
      logged_in = False
      if input('\nWould you like to create an account? (yes/no)\n') == 'yes':
        create_account()
    log_out()
  
  else:
    print('please enter a valid choice')
  print()

def main():
    global loggedin
    user = User()
    while True:
        if logged_in == True: 
            print('Welcome to the DMs\n')
            menu()
        else:
            login(user)
    
    def save_data():  # save data using shelves
      with shelve.open('database') as db:
        db['users'] = user_data
        db['messages'] = message_data
        for key in db:
          print(key, db[key])
    save_data()
    
main()
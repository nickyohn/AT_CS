import shelve
import sys
database_name = 'micro'

class User:
    def __init__(self):
        # user object starts logged out
        global logged_in
        logged_in = False
        with shelve.open(database_name) as data:
            if 'users' not in data:
                data['users'] = {}

    def check_login(self, username, password):
      # checks username and password
      self.username = username
      self.password = password
      success = False
      with shelve.open(database_name) as data:
        # checks for username in user database
          user_data = data['users']
          if username in user_data:
            if password == user_data[username]:
              global logged_in
              logged_in = True
              success = True
      return success
      
    def log_out(self):
        # logs out user
        global logged_in
        logged_in = False

    def save_user(self, username, password):
        # creates a new user in the database
        with shelve.open(database_name) as data:
            user_data = data['users']
            user_data[username] = password
            data['users'] = user_data

class Message:
    def __init__(self):
        with shelve.open(database_name) as data:
            data['messages'] = {}
            data['senders'] = {}
            
    def send(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text
        with shelve.open(database_name) as data:
            sender_data = data['senders']    # dictionary for sender info
            sender_data = {recipient: sender}
            data['senders'] = sender_data:    # dictionary for message info
            message_data = data['messages']
            message_data = {sender: text}
            data['messages'] = message_data

    def show(self, username):
        # show messages
        self.username = username
        with shelve.open(database_name) as data:
            sender_data = data['senders']
            message_data = data['messages']
            if sender_data == {}:
                print('You have no messages at this time.')
            elif message_data == {}:
                print()
            else:
                sender = sender_data[username]
                print(f"@{sender} says: {message_data[sender]}")

def login(user):
    # enter login info 
    user = User()
    print('---------------------')
    print('Login Screen.')
    global username
    username = input('What is your username? ')
    password = input('What is your password? ')
    if user.check_login(username, password):
        print('Success!')
        global logged_in
        logged_in = True
    else:
        print('Sorry, your username or password is incorrect.')
        print('\nChoices')
        print('1: Try again')
        print('2: Create account')
        choice = input('What would you like to do? ') 
        if choice == "1":
          login(user)
        elif choice == '2':
          create_account(user)

def create_account(user):
    # create new account
    username = input('\nCreate a username: ')
    password = input('Create a password: ')
    user.save_user(username, password)

def print_emojis():
    # prints ASCII emojis to use in messages
    print(f"Copy and paste whichever you'd like!")
    print('Shrug: ¯\_(ツ)_/¯')
    print('Concerned: ಠ_ಠ')
    print('Crying: ಥ_ಥ')
    print('Happy: ｡◕‿◕｡')
    print('Annoyed: (¬_¬)')
    print('Shook: (⚆_⚆)')
    print('Animal: (ᵔᴥᵔ)')

def menu(user, message):
    print('---------------------')
    print('Menu Choices')
    print('1: Send a message')
    print('2: Show messages')
    print('3: Show emojis')
    print('4: Log out')
    print('5: Quit')
    choice = input('What would you like to do? ')    
    if choice == '1':   # post a message
        print('Send message\n')
        recipient = input('Enter recipient: ')
        text = input('Enter message: ')
        message.send(username, recipient, text)   
    elif choice == '2':   # show messages
        print('Show messages\n')
        message.show(username)
    elif choice == '3':   # show emojis
        print('Show emojis\n')
        print_emojis()
    elif choice == '4':   # log out
        print('Log out')
        user.log_out()
    elif choice == '5':   # quit 
        print("Bye!")
        sys.exit()        
    else:
        print('Please enter a valid choice')
    print()

def main():
    user = User()
    message = Message()
    print('Welcome to THE PACKER DIRECT MESSAGES')
    while True:
        if logged_in == True:
            menu(user, message)
        else:
            login(user)

main()

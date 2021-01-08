# This is a direct-messaging application made by Nick Yohn. Users can send other users messages (including emojis) and read messages sent to them. 
    # Users can also add in profile information, log out, and create new accounts.

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
      # check username and password
      self.username = username
      self.password = password
      success = False
      with shelve.open(database_name) as data:
          user_data = data['users']
          if username in user_data:     # checks for username in user database
            if password == user_data[username]:
              global logged_in
              logged_in = True
              success = True
      return success
      
    def log_out(self):
        # log out
        global logged_in
        logged_in = False

    def save(self, username, password):     # save new user in database
        with shelve.open(database_name) as data:
            user_data = data['users']
            user_data[username] = password
            data['users'] = user_data

class Message:
    def __init__(self):
        with shelve.open(database_name) as data:
            data['messages'] = {}
            data['senders'] = {}
            
    def send(self, sender, recipient, text):      # send message
        self.sender = sender
        self.recipient = recipient
        self.text = text
        with shelve.open(database_name) as data:      # dictionary for sender info
            sender_data = data['senders'] 
            sender_data[recipient] = sender
            data['senders'] = sender_data       # dictionary for message info
            message_data = data['messages']
            message_data[sender] = text
            data['messages'] = message_data

    def show(self, username):     # show messages
        profile = Profile()
        self.username = username    
        with shelve.open(database_name) as data:
            sender_data = data['senders']
            message_data = data['messages']
            if username in sender_data:      # retrieve messages sent to user
                sender = sender_data[username]
                print(f"@{sender} says: {message_data[sender]}")
                if input(f"\nView @{sender}'s profile info? (yes/no) ") == 'yes':
                    print()
                    profile.show(sender)
            else:      # no messages sent to user
                print('You have no messages at this time.')

def login(user):       # enter login info 
    user = User()
    print('----------------------------------------')
    print('Login Screen.')
    global username
    username = input('What is your username? ')
    password = input('What is your password? ')
    if user.check_login(username, password):       # correct username/password
        print('Success!')
        global logged_in
        logged_in = True
    else:       # incorrect username/password
        print('Sorry, your username or password is incorrect.')
        print('\nChoices:')
        print('1: Try again')
        print('2: Create account')
        choice = input('\nWhat would you like to do?')
        if choice == "1":       # try again
            login(user)
        elif choice == '2':
            # create account
            create_account(user)
        else:
            print('Please enter a valid choice')

class Profile:
    def __init__(self):
        with shelve.open(database_name) as data:
            if 'birthday' not in data:
                data['birthday'] = {}
            if 'gender' not in data:
                data['gender'] = {}
            if 'age' not in data:
                data['age'] = {}
            if 'hometown' not in data:
                data['hometown'] = {}

    def save(self, username, birthday, gender, age, hometown):      # save profile info  
        self.username = username
        self.birthday = birthday
        self.gender = gender
        self.age = age
        self.hometown = hometown
        with shelve.open(database_name) as data:
            # birthday 
            birthday_data = data['birthday']
            birthday_data[username] = birthday
            data['birthday'] = birthday_data
            # gender  
            gender_data = data['gender']
            gender_data[username] = gender
            data['gender'] = gender_data
            # age 
            age_data = data['age']
            age_data[username] = age
            data['age'] = age_data
            # hometown 
            hometown_data = data['hometown']
            hometown_data[username] = hometown
            data['hometown'] = hometown_data
    
    def show(self, username):
        # print profile info
        self.username = username
        with shelve.open(database_name) as data:
            birthday_data = data['birthday']
            gender_data = data['gender']
            age_data = data['age']
            hometown_data = data['hometown']
            print(f"@{username}")
            print(f"Birthday: {birthday_data[username]}")
            print(f"Pronouns: {gender_data[username]}")
            print(f"Age: {age_data[username]}")
            print(f"Hometown: {hometown_data[username]}")

def create_account(user):      # create new account
    username = input('\nCreate a username: ')
    password = input('Create a password: ')
    user.save(username, password)

def print_emojis():      # print emojis to use in messages
    print(f"Copy and paste whichever you'd like!")
    print('\nASCII:')
    print('Shrug: ¯\_(ツ)_/¯')
    print('Concerned: ಠ_ಠ')
    print('Crying: ಥ_ಥ')
    print('Happy: ｡◕‿◕｡')
    print('Annoyed: (¬_¬)')
    print('Shook: (⚆_⚆)')
    print('Animal: (ᵔᴥᵔ)')
    print('\nEMOJIS:')
    print('Hot: 🥵')
    print('Kiss: 😘')
    print('Crazy: 🤪')
    print('Eye roll: 🙄')
    print('Fuming: 😤')
    print('Sunglasses: 😎')
    print('Mind blown: 🤯')
    print('Disappointed: 😔')
    print('Pleased: 😌')
    print('Poop: 💩')

def menu(user, message, profile):
    print('----------------------------------------')
    print('Menu Choices')
    print('0: Enter profile info')
    print('1: View profile info')
    print('2: Send a message')
    print('3: Show messages')
    print('4: View emojis')
    print('5: Log out')
    print('6: Quit')
    print('----------------------------------------')
    choice = input('What would you like to do? ')    
    
    if choice == '0':     # enter profile info
        print('Enter profile info\n')
        birthday = input('Enter birthday (mm/dd/yyyy): ')
        gender = input('Enter pronouns: ')
        age = input('Enter age: ')
        hometown = input('Enter hometown: ')
        profile.save(username, birthday, gender, age, hometown)

    if choice == '1':      # view profile info
        print('View profile info\n')
        with shelve.open(database_name) as data:
            birthday_data = data['birthday']        # checks if user has entered any profile info
            if username not in birthday_data:   
                print('You have not entered any profile info.')
            else:
              profile.show(username) 
                
    if choice == '2':     # post a message
        print('Send message\n')
        recipient = input('Enter recipient: ')
        text = input('Enter message: ')
        message.send(username, recipient, text)   

    elif choice == '3':     # show messages
        print('Show messages\n')
        message.show(username)

    elif choice == '4':     # view emojis
        print('View emojis\n')
        print_emojis()

    elif choice == '5':     # log out
        print('Log out')
        user.log_out()

    elif choice == '6':     # quit 
        print("Bye!")
        sys.exit()    

    else:
        print('Please enter a valid choice')
    print()

def main():
    profile = Profile()
    user = User()
    message = Message()
    print('Welcome to The Packer Direct Messages 🎉')
    while True:
        if logged_in == True:
            menu(user, message, profile)
        else:
            login(user)

main()

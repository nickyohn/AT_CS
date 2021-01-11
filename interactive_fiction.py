# this could be written a lot better, so please make changes where necessary.

import sys

# opening scene
def intro_scene():    
  print("Indiana Jones’s Escape from the Pyramid of Ra\n")
  print("Indiana Jones: *walks through the hallway of the secret pyramid of Cleopatra, eventually he walks into a room and the door shuts behind him*\n")
  print("Unknown Voice: Welcome, Henry Jones.\n")
  print("Indiana Jones: *Whips out revolver* Reveal yourself! Get out of hiding, whoever you are? And...how did you know my name?\n")
  print("Unknown Voice: Ahh, I forgot. You mortals fear that which you don’t know. Such a limitation that is...shameful. You may know me by the name Cleopatra. Yes...the Cleopatra, lover to Caesar and Marcus Antonius. If you want my treasures, you’ll have to solve my traps. Obviously, success means you get my treasures. Failure means...death.\n")
  print("Indiana Jones: *Shoots at walls, hoping to shoot through it and kill whoever may be behind those walls.*\n")
  print("Cleopatra: *laughs* Ah...you pitiful humans. I indeed am speaking to you from beyond the grave, no amount of bullets you fire from your revolver can do harm to me.\n")
  print("Indiana Jones: *after wasting a good chunk of his ammo* Fine, then. What have you got in store for me?\n")
  print("Cleopatra: Wonderful…\n")
  print("*Roof opens, and a large stone slab is slowly sliding down. This stone slab is heavy enough to crush anyone with ease, but it’s also got spears attached to it, making an already gruesome death worse.*\n")
  print("Cleopatra: You have 2 minutes to solve each puzzle. You have to decipher what I’m saying and repeat it back to me in English. I should note you are allowed to use any necessary books you brought with you to solve this. Should you succeed, you may move on to the next puzzle. Should you fail...well, it’s not hard to see what fate will befall you if you fail…\n")
  
  global intro_done
  intro_done = True
  

#--------------------------------------------------
# room one

def translation_one():
  print("1: The enemies of Caesar killed my husband in the forum.")
  print("2: The enemies of Caesar in the forum killed my husband.")
  print("3: In the forum did Caesar’s enemies kill my husband.")

def room_one():
  print("Cleopatra: In forum inimici Caesari necaverunt virum mihi.")
  print("dIndiana Jones: (choose which of the following is the correct translation in Latin).")

  global fail_counter
  fail_counter = 0

  translation_one()
 
  choice = input("Answer: ")

  if choice == "1":
    print ("Wrong, Henry. You get one more chance.")
    global fail_counter
    fail_counter += 1
    translation_one()  
  elif choice == "2":
    print ("Wrong, Henry. You get one more chance.")
    global fail_counter
    fail_counter += 1
    translation_one()
  elif choice == "3":
    print("Cleopatra: Ahh, yes. Correct. You humans are not as stupid as you seem…")
    global room_one_done
    room_one_done = True
  else:
    print("Please enter a valid answer.")
    room_one()


#--------------------------------------------------
# room two

def translation_two():
  print("Upon my death, Egypt held power no more. We were weak. The Romans defeated us. For this reason I was most distressed.")
  print("Upon my death, Egypt did not hold power. We were very weak. The Romans defeated us. For this reason, I’m very depressed.")

def room_two():
  print("Cleopatra: super morte mihi, Aegyptus non habuit potentiam. Eramus tenerrimi... Romani vicerunt nostros... Ob eam causam dolorissima eram.")
  translation_two()
  choice = input("Answer: ")

  if choice == "1":
    print("Cleopatra: Well done, Henry. Well done. Your final challenge awaits you.")
    global room_two_done
    room_two_done = True
    
  elif choice == "2":
    global fail_counter
    fail_counter += 1 
    if fail_counter < 2:
      print("Wrong, Henry. You get one more chance.")
      translation_two()
    else:
      print("You disappoint me, “Indiana Jones”. I truly thought you stood a chance. Evidently, I was wrong. Goodbye.")
      sys.exit()
  else:
    print("Please enter a valid answer.")
    room_two()
    

#--------------------------------------------------
# room three

def translation_three():
  print("Your next task in this is...tell to me my family tree.")
  print("Your next task is...tell me my family tree.")

def room_three():
  print("Cleopatra: Alright, “Indiana Jones,” I’ve got one more section of this puzzle for you.\n")
  print("Proxi aeruma tibi in hoc est...dic mihi arborem gentis mei.")
  choice = input("Answer: ")

  if choice == "1":
    global fail_counter
    fail_counter += 1
    if fail_counter < 2:
      print("Cleopatra: No matter, you have already proved your knowledge in this aspect. Not close to mine, for sure, but not bad. Please proceed through the door I’ve just opened to claim your prize.")
      global room_three_done
      room_three_done = True
    else:
      print("Cleopatra: I’m afraid I’ve given you too many chances….You know what happens now. Recquiescas in pace.")
      sys.exit()

  elif choice == "2":
    print("Cleopatra: Ah, I see you are a fellow erudite. You have my respect. Please, step through the door to claim your prize.")
    global room_three_done
    room_three_done = True


#--------------------------------------------------
# prize room

def prize_room():
  print("Cleopatra: My treasure was sought out by many. Many who thought that they could throw money at the problem to collect what was not theirs to begin with. Some men brought large militaries and tried using C4 to blow down the walls and steal my treasure. I tried to warn them that there was nothing to steal and that the walls had my blessing, making them invincible, but they wouldn’t listen. I...taught them a lesson. Now they are with me, as my thralls eternally in the afterlife.\n")
  print("But I digress, claim your treasure, Henry Jones!")

  if fail_counter == 1:
    print("Cleopatra: My amulet stands before you. I used to wear it as a child, but seeing as I am no longer a child and an immortal deity, I’ve altered it a bit. Wearing it now grants the wearer a one time revival should you meet your end prematurely, and greatly increased stamina, strength, and skill with any weapon he lays his hands on.")

  if fail_counter == 0:
    print("Cleopatra: *Blesses Indiana Jones’s whip, it glows with a bright white.* I’ve taken the liberty of blessing your whip, but it relies on your power and your state of mind. If you feel weak and hopeless, this whip is as if I never blessed it. But if your heart is pure with righteousness, it will glow a bright white and allow you to bend the very reality you live in. Its powers are endless. Not to mention that for as long as it glows white, you are invulnerable. Go forth, “Indiana Jones,” and spread that righteousness.")

  print("Indiana Jones: Thank you very much, Cleopatra. Righteousness shall be spread, and I will be the one to spread it. ")


def main():
  intro_scene()
  if intro_done == True:
    room_one()
    if room_one_done == True:
      room_two()
      if room_two_done == True:
        room_three()
        if room_three_done == True:
          prize_room()

main()
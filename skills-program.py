import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import sqlite3
from time import sleep
import re
from tkinter import END
import pyautogui
# Creating the Databases:
# register Database:
db_register = sqlite3.connect("register_database.db")
db_register.execute("create table if not exists users(name text, username text, user_ID text, password text, phone text)")
cr_register = db_register.cursor()
userNames = cr_register.execute("select username from users")
userNames_get = userNames.fetchall()
user_IDs = cr_register.execute("select user_ID from users")
user_IDs_get = user_IDs.fetchall()
# skills database:
db_skills = sqlite3.connect("skills_database.db")
db_skills.execute("create table if not exists skills(username text, skill text, progress integer)")
cr_skills = db_skills.cursor()
skills_users_select = cr_skills.execute("select username from skills")
skills_users_get = skills_users_select.fetchall()
skills_skill_select = cr_skills.execute("select skill from skills")
skills_skill_get = skills_skill_select.fetchall()
skills_progress_select = cr_skills.execute("select progress from skills")
skills_progress_get = skills_progress_select.fetchall()

# Program Functions
def exitProgram():
  yesblue = convert_blue("yes")
  noblue = convert_blue("no")
  exit_input = input(f"Do you want to exit the brogram ({yesblue}, {noblue}): ").capitalize().strip()
  if exit_input == "No" or exit_input == "N":
    skillsRecord()
  elif exit_input == "Yes" or exit_input == "Y":
    redslowprint("Exeting the program ")
    red_dots_delay()
    red_dots_delay()
    redslowprint("Exit completed")
    sleep(1)
    END
  else:
    print("please choose (Yes, NO) only")
    exitProgram()
# dots_delay functions
def dots_delay(s = 1):
  print(" . ", end="")
  sleep(s)
  print(" . ", end="")
  sleep(s)
  print(" . ", end="")
  sleep(s)
def blue_dots_delay(s = 1):
  print(Fore.BLUE +" . ", end="")
  sleep(s)
  print(Fore.BLUE +" . ", end="")
  sleep(s)
  print(Fore.BLUE +" . ", end="")
  sleep(s)
def yellow_dots_delay(s = 1):
  print(Fore.YELLOW +" . ", end="")
  sleep(s)
  print(Fore.YELLOW +" . ", end="")
  sleep(s)
  print(Fore.YELLOW +" . ", end="")
  sleep(s)
def green_dots_delay(s = 1):
  print(Fore.GREEN +" . ", end="")
  sleep(s)
  print(Fore.GREEN +" . ", end="")
  sleep(s)
  print(Fore.GREEN +" . ", end="")
  sleep(s)
def green_dots_delay(s = 1):
  print(Fore.GREEN +" . ", end="")
  sleep(s)
  print(Fore.GREEN +" . ", end="")
  sleep(s)
  print(Fore.GREEN +" . ", end="")
  sleep(s)
def red_dots_delay(s = 1):
  print(Fore.RED +" . ", end="")
  sleep(s)
  print(Fore.RED +" . ", end="")
  sleep(s)
  print(Fore.RED +" . ", end="")
  sleep(s)
def blackonwhite_dots_delay(s = 1):
  print(Fore.BLACK + Back.WHITE +" . ", end="")
  sleep(s)
  print(Fore.BLACK + Back.WHITE +" . ", end="")
  sleep(s)
  print(Fore.BLACK + Back.WHITE +" . ", end="")
  sleep(s)
# Print Functions 
def redprint(text, endr="\n"):
  print(Fore.RED + text, end=endr) 
def yellowprint(text, endr="\n"):
  print(Fore.YELLOW + text, end=endr)
def greenprint(text, endr="\n"):
  print(Fore.GREEN + text, end=endr)
def blueprint(text, endr="\n"):
  print(Fore.BLUE + text, end=endr)
def blackonwhiteprint(text, endr="\n"):
  print(Fore.BLACK + Back.WHITE + text, end=endr)
# convert string color functions
def convert_blue(text):
  conv_text = Fore.BLUE + text
  return conv_text + Fore.RESET
def convert_red(text):
  conv_text = Fore.RED + text
  return conv_text + Fore.RESET
def convert_green(text):
  conv_text = Fore.GREEN + text
  return conv_text + Fore.RESET
def convert_yellow(text):
  conv_text = Fore.YELLOW + text
  return conv_text + Fore.RESET
# slow print function:
def slowprint(text, delay =0.1):
  text_container = []
  for i in text:
    text_container.append(i)
  for i in text_container:
    print(f"{i}", end="")
    sleep(delay)
  print("")
def redslowprint(text, delay =0.1):
  text_container = []
  for i in text:
    text_container.append(i)
  for i in text_container:
    print(Fore.RED + f"{i}", end="")
    sleep(delay)
  print("")
def blueslowprint(text, delay =0.1):
  text_container = []
  for i in text:
    text_container.append(i)
  for i in text_container:
    print(Fore.BLUE +  f"{i}", end="")
    sleep(delay)
  print("")
def yellowslowprint(text, delay =0.1):
  text_container = []
  for i in text:
    text_container.append(i)
  for i in text_container:
    print(Fore.YELLOW + f"{i}", end="")
    sleep(delay)
  print("")
def greenslowprint(text, delay =0.1):
  text_container = []
  for i in text:
    text_container.append(i)
  for i in text_container:
    print(Fore.GREEN + f"{i}", end="")
    sleep(delay)
  print("")
# Progress bar funcion
def progress_Bar(progress, total):
  percent = 100 * (progress/ float(total))
  bar = '|'* int(percent) + '-'*(100 - int(percent))
  print(f"\r |{bar}| {percent:.2f}%", end="\n")
# Dynamic progress bar:
def dynamic_progress_Bar(progress, total):
  percent = 100 * (progress/ float(total))
  bar_container = []
  for i in range(0, int(percent)):
    bar_container.append('|')
  for x in range(0, (100 - int(percent))):
    bar_container.append('-')
  start_time_delay = 0.01
  for item in range(0,100):
    print(f"{bar_container[item]}", end="")
    sleep(start_time_delay)
    if start_time_delay > 0.001:
      start_time_delay -= 0.001
    else:
      pass
  print(f" {percent:.2f}%", end="\n")
# Colored Dynamic progress bar:
def colored_dynamic_progress_Bar(progress, total):
  percent = 100 * (progress/ float(total))
  bar_container = []
  for i in range(0, int(percent)):
    if int(percent) in range(0,26):
      bar_container.append(Fore.RED + '|')
    elif int(percent) in range(26,51):
      bar_container.append(Fore.YELLOW + '|')
    elif int(percent) in range(51,76):
      bar_container.append(Fore.BLUE + '|')
    elif int(percent) in range(76,101):
      bar_container.append(Fore.GREEN + '|')
    else:
      print("An error happend durint calculating the color of the percent")
    
  for x in range(0, (100 - int(percent))):
    bar_container.append('-')
  start_time_delay = 0.01
  for item in range(0,100):
    print(f"{bar_container[item]}", end="")
    sleep(start_time_delay)
    if start_time_delay > 0.001:
      start_time_delay -= 0.001
    else:
      pass
  print(f" {percent:.2f}%", end="\n")
# Main program start point funciont 
def skillsRecord():
  #Global program variables
  yesblue = convert_blue("yes")
  noblue = convert_blue("no")
  sblue = convert_blue("s")
  ablue = convert_blue("a")
  dblue = convert_blue("d")
  ublue = convert_blue("u")
  qblue = convert_blue("q")
  input_messege = f"""
  please tell us what you want to do:
  {sblue} ==> show my skills
  {ablue} ==> Add new skill
  {dblue} ==> delete a skill
  {ublue} ==> update a skill progress
  {qblue} ==> quite the app
  enter your choice here: """
  # main pogram functions 
  def signUp():
    def nameInput():
      global signupName
      signupName= input("Please Enter your Name: ").strip().capitalize()
      def checkName():
        if signupName == "":
          redprint('Sorry this field is required. Please input a valid name')
          nameInput()
        else:
          return True
      checkName()
      if checkName() is True:
        return signupName
    nameInput()
    def usernameInput():
      global signupUsername
      signupUsername= input("Please Enter your prefered Username: ").strip()
      def checkUsername():
        signupUsername_checker = (f'{signupUsername}',)
        if signupUsername_checker in userNames_get:
          redprint("Sorry this user name is already taken. please enter another user name")
          red_dots_delay(0.25)
          red_dots_delay(0.25)
          usernameInput()
        else:
          return True
      checkUsername()
      if checkUsername() is True:
        return signupUsername
    usernameInput()
    def PhoneInput():
      global signupPhone
      signupPhone = input("Please Enter your phone number: ").strip()
      checker = re.findall(r"([A-z])(\s)", signupPhone)
      def checkPhone():
        if checker == []:
          return True
        else:
          redprint("please do not include any charachters or white spaces in your phone number.", end= "")
          red_dots_delay(0.25)
          red_dots_delay(0.25)
          print( "You can try again")
          PhoneInput()
      checkPhone()
      if checkPhone is True:
        return signupPhone
    PhoneInput()
    def passwordInput():
      global signupPassword
      signupPassword= input("Please Enter your password (At least 8 charachters long): ")
      def checkPassword():
        if signupPassword =="":
          redprint("Please do not leave this field empty. Password is required", "")
          red_dots_delay()
          red_dots_delay()
          passwordInput()
        elif len(signupPassword) < 8:
          redprint("sorry your password should be more than 8 charachter long. please try again", "")
          red_dots_delay(3)
          red_dots_delay(3)
          passwordInput()
        else:
          return True
      checkPassword()
      if checkPassword() is True:
        pass
    passwordInput()
    def passwordAgainInput():
      signupPasswordAgain = input("Please enter your password again: ")
      def checkPasswrdAgain():
        global checker_password
        checker_password = None
        if signupPasswordAgain == signupPassword:
          checker_password = True
        else:
          redprint("Sorry the password does not match")
          red_dots_delay(0.45)
          red_dots_delay(0.45)
          return False
      checkPasswrdAgain()
      
      if checker_password == True:
        pass
      else:
        def optionInput():
            option = input("type (r) to re-enter password again or type (p) to reset the main password: ").strip().lower()
            if option == "r":
              passwordAgainInput()
            elif option == "p":
              passwordInput()
              passwordAgainInput()
            else:
              redprint("sorry we did not recognize your answer. Please try again")
              red_dots_delay(0.35)
              red_dots_delay(0.35)
              optionInput()
        optionInput()
    passwordAgainInput()
    def insertion():
      IDs = len(user_IDs_get) #importing from database section above
      cr_register.execute(f"insert into users(username, name, phone, password, user_ID ) values('{signupUsername}','{signupName}', '{signupPhone}', '{signupPassword}', {IDs + 1})")
      db_register.commit()
      cr_skills.execute(f"insert into skills(username) values('{signupUsername}')")  
      db_skills.commit()
      dots_delay()
      dots_delay()
      greenprint(f"You signed up successfully,")
      print("-"*100)
      print("-"*100)
      blueprint(f"{signupName}")
      def option():
        inblue = convert_blue("in")
        qblue = convert_blue("q")
        signoption = input(f"type ({inblue}) to sign in or type ({qblue}) to quit the program: ").lower().strip()
        if signoption == "in" or signoption == "i":
          signIn()
        elif signoption == "quite" or signoption == "q":
          exitProgram()
        else:
          redprint("sorry we did't recognize your answer. Please try again")
          red_dots_delay(0.35)
          red_dots_delay(0.35)
          option()
      option()
    insertion()
  def signIn():
    def signinUsernameinput():
      usernames_select = cr_register.execute("select username from users")
      user_get_all = usernames_select.fetchall()
      global signinUsername
      signinUsername = input("Please enter your Username: ").strip().lower()
      def checkUsername():
        signinUsername_checker = (f'{signinUsername}',)
        if signinUsername_checker in user_get_all:
          return True
        else:
          redprint("This username is not found.")
          sleep(1.5)
          print(" Please make sure you write the user name correctly.")
          sleep(2)
          def retry():
            username_option = input("type (r) to enter your user name again or type (up) to sign up: ").lower().strip()
            if username_option == "r":
              signinUsernameinput()
            elif username_option == "up" or username_option == "u" or username_option == "signup":
              signUp()
            elif username_option == "":
              redprint("You cannot leave this field empty. ","")
              dots_delay(0.5)
              print("Please try again")
              sleep(2)
              retry()
            else:
              redprint("Sorry we did't recognize your answer. ","")
              dots_delay(0.5)
              print("Please try again")
              sleep(2)
              retry()
              return False
          retry()
      if checkUsername() is True:
        pass
    signinUsernameinput()
    def signinPasswordinput():
      print(f"hello, ",end="")
      blueprint(f"{signinUsername}")
      signinpasswordinput = input("Please enter your Password: ").strip()
      signinpasswordinput_checker = (f'{signinpasswordinput}',)
      password_select = cr_register.execute(f"select password from users where username = '{signinUsername}'")
      password_get_all = password_select.fetchall()
      def signinpasswordcheck():
        if signinpasswordinput_checker in password_get_all:
          greenprint("Signing in")
          green_dots_delay(0.5)
          green_dots_delay(0.5)
          green_dots_delay(0.5)
          print("signing in completed")
          main()
        elif signinpasswordinput == "":
          redprint("You cannot leave this field empty. ", "")
          red_dots_delay(0.3)
          red_dots_delay(0.3)
          print("Please try again", end = "")
          sleep(2)
          signinPasswordinput()
        else:
          redprint("Password is incorrect. ", "")
          red_dots_delay(0.3)
          red_dots_delay(0.3)
          print("Please try again", end = "")
          sleep(2)
          signinPasswordinput()
      signinpasswordcheck()
    signinPasswordinput()
  def main():
    sleep(2)
    print(f"\n Hello, {convert_blue(signinUsername)} in the program")
    main_option= input(input_messege).strip().lower()
    def showSkill():
        blueslowprint("showing all skills")
        blue_dots_delay(0.3)
        blue_dots_delay(0.3)
        print("", end="\n")
        current_user_skills_select = cr_skills.execute(f"select skill from skills where username = '{signinUsername}'")
        current_user_skills_fetsh = current_user_skills_select.fetchall()
        current_user_progress_select = cr_skills.execute(f"select progress from skills where username = '{signinUsername}'")
        current_user_skills_fetsh = current_user_progress_select.fetchall()
        current_user_all_select = cr_skills.execute(f"select * from skills where username = '{signinUsername}'")
        current_user_all_fetsh = current_user_all_select.fetchall()
        skill_counter = 1
        for username, skill, progress in current_user_all_fetsh:
          blueprint(f"{username}",""); print(": skill=",end=""); blueprint(f"{skill_counter}",""); print("==>",end="");blueprint(f" {skill}",""); print(",progress: %",end=""); blueprint(f" {progress}")
          colored_dynamic_progress_Bar(int(progress),100)
          skill_counter +=1
        main() 
    def addSkill():
      current_user_skills_select = cr_skills.execute(f"select skill from skills where username = '{signinUsername}'")
      current_user_skills_fetsh = current_user_skills_select.fetchall()
      skill_add_name = input("please enter the name of the new skill: ").strip() 
      def progress_checker():
        global skill_add_progress
        skill_add_progress = int(input("please enter the progress of the new skill(0-100): " + "%"))
        if skill_add_progress > 100:
          redprint("sorry this field only accepts values from 0 to 100. ")
          red_dots_delay(0.3)
          red_dots_delay(0.3)
          print("Please try again")
          sleep(2)
          progress_checker()
        elif str(skill_add_progress) == "":
          print("Sorry, you can't leave this field empty. Please try again.")
          red_dots_delay(0.3)
          red_dots_delay(0.3)
          print("If you do not have progress yet, you can type: 0 ")
          sleep(2)
          print("Please try again")
          sleep(2)
          progress_checker()
        else:
          return skill_add_progress
      progress_add_holder= progress_checker()
      cr_skills.execute(f"insert into skills(username, skill, progress) values('{signinUsername}', '{skill_add_name}', '{progress_add_holder}')")
      db_skills.commit()
      blueprint("Adding skill")
      blue_dots_delay(0.35)
      blue_dots_delay(0.35)
      greenprint("skill added succesfully","")
      green_dots_delay()
      main()
    def deleteSkill():
      delete_skill_input= input("please type the name of the skill you want to delete: ").strip()
      current_user_skills_select = cr_skills.execute(f"select skill from skills where username = '{signinUsername}'")
      current_user_skills_fetsh = current_user_skills_select.fetchall()
      delteSkill_checker = (f'{delete_skill_input}',)
      if delteSkill_checker in current_user_skills_fetsh:
        def delete_Option():
          option_del = input(f"Are you sure you want to delete this skill ({yesblue}, {noblue}): ").lower().strip()
          if option_del == "yes" or option_del == "y":
            cr_skills.execute(f"Delete from skills where (username = '{signinUsername}' and skill = '{delete_skill_input}')")
            redprint ("Skill is deleting","")
            dots_delay()
            dots_delay()
            greenprint("Skill deleted succefully")
            main()
          elif option_del == "no" or option_del == "n":
            main()
          elif option_del == "":
            redprint (f"Sorry, you can't leave this field empty. Please type a valid option ({yesblue}), {noblue})")
            sleep(3)
            delete_Option()
          else:
            redprint ("Sorry we didn't understand what you typed. Please, enter a valid option (yes, no)")
            delete_Option()
        delete_Option()
      else:
        redprint(f"We did't found a skill with name: {delete_skill_input}, please make sure you enter the name correctly")
        deleteSkill()
    def updateskill():
      update_skill_input = input("Please enter the name of the skill to be updated: ").strip()
      current_user_skills_select = cr_skills.execute(f"select skill from skills where username = '{signinUsername}'")
      current_user_skills_fetsh = current_user_skills_select.fetchall()
      updateSkill_checker = (f'{update_skill_input}',)
      if updateSkill_checker in current_user_skills_fetsh:
        def update_Option():
          option_update = input(f"Are you sure you want to update the data of this skill ({yesblue}, {noblue}): ").lower().strip()
          if option_update == "yes" or option_update == "y":
            new_name = input("what is the new updated name of this skill: ").strip()
            new_progress = int(input("what is the new updated progress of this skill (0-100): %" ).strip())
            cr_skills.execute(f"update skills set skill = '{new_name}', progress = {new_progress} where (username = '{signinUsername}' and skill = '{update_skill_input}')")
            db_skills.commit()
            blueprint ("Skill is Updating")
            blue_dots_delay()
            blue_dots_delay()
            greenprint(f"Skill is updated succefully")
            sleep(2)
            main()
          elif option_update == "no" or option_update == "n":
            main()
          elif option_update == "":
            redprint ("Sorry, you can't leave this field empty. Please type a valid option (yes, no)")
            red_dots_delay(0.5)
            red_dots_delay(0.5)
            update_Option()
          else:
            redprint ("Sorry we didn't understand what you typed. Please, enter a valid option (yes, no)")
            red_dots_delay(0.5)
            red_dots_delay(0.5)
            update_Option()
        update_Option()
      else:
        redprint(f"We did't found a skill with name: {convert_blue(update_skill_input)}, please make sure you enter the name correctly")
        red_dots_delay(0.5)
        red_dots_delay(0.5)
        updateskill()  
    def quitApp():
      re_asure = input(f"Are you sure you want to quit the app ({yesblue}, {noblue}): ").strip().lower()
      if re_asure == "yes" or re_asure =="y":
        END
      elif re_asure == "no" or re_asure =="n":
        main()
      elif re_asure == "":
        redprint("you can't leave this field empty. ","")
        red_dots_delay(0.3)
        red_dots_delay(0.3)
        print("Please try again")
        sleep(2)
        quitApp()
      else:
        redprint("Sorry we did not recognize your answer.", "")
        red_dots_delay()
        red_dots_delay()
        print("Please try again.")
        quitApp()
    def makeaction():
      if main_option == "s":
        showSkill()
      elif main_option == "a":
        addSkill()
      elif main_option == "d":
        deleteSkill()
      elif main_option == "u":
        updateskill()
      elif main_option == "q":
        quitApp()
      elif main_option == "":
        redslowprint("Sorry you can't leave this field epmty. Plese choose a valid answer", 0.05)
        red_dots_delay(0.3)
        red_dots_delay(0.3)
        main()
      else:
        redslowprint("Sorry we did not recognize your answer. Plese choose a valid answer", 0.05)
        red_dots_delay(0.3)
        red_dots_delay(0.3)
        main()
    makeaction()
  def registeration():
    blueslowprint("Hello to the Skills Progress APP")
    sleep(3)
    inblue = convert_blue("in")
    upblue = convert_blue("up")
    opt_Regester = input(f"To Sign In type ({inblue}) or to Sign up type ({upblue}): ").strip().lower()
    if opt_Regester == "up" or opt_Regester == "u":
      signUp()
    elif opt_Regester == "in":
      signIn()
    else:
      redprint ("Sorry, we did't recognize your answer", "")
      red_dots_delay()
      print("Please try again")
      sleep(2)
      registeration()
  registeration()
skillsRecord()
cr_register.close()
cr_skills.close()
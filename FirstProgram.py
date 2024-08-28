#FirstProgram.py
#Name:Max Perry
#Date:8/28/2024
#Assignment:FristProgram

def main():
  print("First Program")
  #Say hello
  print("hello")
  #Ask for the user's name
  name=input("What is your name?")
  #Use the user's name in the program.
  input("How are you today "+name+"?")
  #Ask the user for their age.
  age=input("How old are you "+name+"?")
  age=int(age)
  birthyear=2024-age
  #Tell the user what year they were born in.
  print (name,", you were born in ",birthyear)
  #Assume that they have not had their birthday yet this year.

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()

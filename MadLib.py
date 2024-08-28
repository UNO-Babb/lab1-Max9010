#MadLib.py
#Name:Max Perry
#Date:8/28/2024
#Assignment:MadLib

def main():
  print("Madlib")
  #Ask user for words
  noun1= input("Please enter a noun. ")
  verb1= input("Please enter a verb. ")
  animal1= input("Please enter an animal. ")
  verb2= input("Please enter a verb. ")
  adjective1= input("Please enter a adjective. ")
  noun2= input("Please enter a noun. ")
  #Print the story with the user supplied words.
  print("Once upon a time there was a " + noun1 + ".")
  print("It was very a scary " + noun1 + " that loved to " + verb1 + ".")
  print("One day the " + noun1 + " was stumbled upon by a small little " +animal1+".")
  print("The "+animal1+" laughed, played, and "+verb2+"ed.")
  print("I can't thing of anything else" ,adjective1,noun2+".")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()

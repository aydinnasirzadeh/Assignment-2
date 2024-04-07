#import libraries here

def main():
  n=input("Enter a letter of the alphabet: ")
  if n=="a" or n=="e" or n=="i" or n=="o" or n=="u":
      print("Entered alphabet is a vowel!")
  elif n=="y":
      print("Sometimes it is a vowel, and sometimes it is a consonant!")
  else:
      print("Entered alphabet is a consonant! ")
  pass

if __name__ == "__main__":
  main()

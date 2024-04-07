#import libraries here

def main():
  lttr=input("Enter a letter of the alphabet: ")
  if lttr=="a" or lttr=="e" or lttr=="i" or lttr=="o" or lttr=="u":
    print("Entered alphabet is a vowel!")
  elif lttr=="y":
    print("Sometimes it is a vowel, and sometimes it is a consonant!")
  else:
    print("Entered alphabet is a consonant!")
  pass

if __name__ == "__main__":
  main()

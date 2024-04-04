def main():
    inp = input("Enter a letter of the alphabet: ")
    saitler = ['a','e','i','o','u']
    if inp in saitler:
        print("Entered alphabet is a vowel!")
    elif inp != 'y':
        print("Entered alphabet is a consonant!")
    else:
        print("Sometimes it is a vowel, and sometimes it is a consonant!")
    pass

if __name__ == "__main__":
  main()

def main():
    inp = (int)(input("Enter the wavelength in nm: "))
    ans = None
    if inp <380:
        ans = None
    elif inp <450:
        ans = 'Violet'
    elif inp <495:
        ans = 'Blue'
    elif inp < 570:
        ans = 'Green'
    elif inp < 590:
        ans = 'Yellow'
    elif inp < 620:
        ans = 'Orange'
    elif inp <= 750:
        ans = 'Red'
    if not ans:
        print("Invalid input!")
    else:
        print(f'The relevant color is {ans}')
    pass

if __name__ == "__main__":
  main()

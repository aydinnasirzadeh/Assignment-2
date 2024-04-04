def main():
    data = [
    "Dragon",
    "Snake",
    "Horse",
    "Sheep",
    "Monkey",
    "Rooster",
    "Dog",
    "Pig",
    "Rat",
    "Ox",
    "Tiger",
    "Hare"
    ]
    inp = (int)(input("Enter the year [ex. 2021]: "))
    if inp < 0:
        print("Invalid year!")
    else:
        print(f'{inp} is the year of the {data[(inp%12+4)%12]}')

if __name__ == "__main__":
  main()

#i feel myself like as i hired hourly -_-
#i hope this type of bullshits shouldn't come in exam

def main():
    inp1 = input("Enter a month [ex. March]: ")
    inp2 = (int)(input("Enter the day [ex. 12]: "))
    
    data = ["Capricorn December 22 to January 19",
"Aquarius January 20 to February 18",
"Pisces February 19 to March 20",
"Aries March 21 to April 19",
"Taurus April 20 to May 20",
"Gemini May 21 to June 20",
"Cancer June 21 to July 22",
"Leo July 23 to August 22",
"Virgo August 23 to September 22",
"Libra September 23 to October 22",
"Scorpion October 23 to November 21",
"Sagittarius November 22 to December 21"]
    ans=None
    if inp2 < 0:
        print("Either a month or a day is invalid!")
        return
    if inp1 == 'February' and inp2 == 30:
        print("Either a month or a day is invalid!")
        return
    if inp1 == 'November' and inp2 == 31:
        print("Either a month or a day is invalid!")
        return       
    if inp1 == 'June' and inp2 == 31:
        print("Either a month or a day is invalid!")
        return
    for i in data:
        i=i.split()
        if (inp1==i[1] and (inp2>=(int)(i[2]) and inp2<=31)) or (inp1==i[4] and (inp2<=(int)(i[5]) and inp2<=31)):
            ans=i[0]
    if not ans:
        print("Either a month or a day is invalid!")
    else:
        print(f'Your zodiac sign is {ans}')
    pass

if __name__ == "__main__":
  main()

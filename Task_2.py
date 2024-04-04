def main():
    month = [	
        'January',
		'February',
		'March',
		'April',
		'May',
		'June',
		'July',
		'August',
		'September',
		'October',
		'November',
		'December'
	]
    inp1 = (input("Enter name of the month [ex. June]: "))
    inp2 = (int)(input("Enter the day [ex. 5]: "))
    
    ind = [idx for idx, i in enumerate(month) if i == inp1][0]
    if (ind==2 and inp2>=20) or ((ind==3)+(ind==4)) or (ind==5 and inp2<21):
        print(f'{inp1} {inp2} is in Spring')
    elif(ind==5 and inp2>=21) or ((ind==6)+(ind==7)) or (ind==8 and inp2<22):
        print(f'{inp1} {inp2} is in Summer')
    elif (ind==8 and inp2>=22) or ((ind==9)+(ind==10)) or (ind==11 and inp2<21):
        print(f'{inp1} {inp2} is in Fall')
    else:
        print(f'{inp1} {inp2} is in Winter')
    
    pass

if __name__ == "__main__":
  main()

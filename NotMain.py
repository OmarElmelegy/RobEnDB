import datetime

def DataInput():
    try: 
        name,givendate = input("Enter a name & Date of birth: ").split(",")
        CapitalizedName = name.title()
        a,b,c = givendate.split("/")
        newdate = datetime.date(int(c),int(b),int(a))
        age = datetime.date.today().year - newdate.year
        if(age <= 0):
            print("Enter valid date of birth")
            DataInput()
        with open("Database.txt",'a') as f:
            f.write(f"{CapitalizedName},{age}\n")
    except:
        print("Enter valid inputs")
    
    print("\n")

def DataOutput():
    with open("Database.txt",'r') as r:
        for line in r:   
            outname,outage = line.split(",")
            print(f"{outname}, {outage.strip()} years old")
    print("\n")
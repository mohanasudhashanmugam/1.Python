class multipleFunctions():
    def Subfields():
        print("Subfields in AI are: \nMachine Learning \nNeural Networks \nVision \nRobotics \nSpeech Processing \
    \nNatural language processing")
        
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,' is Even number')
        else:
            print(num,' is Odd number')
            
    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(age>=18 and gender.upper()=='FEMALE') or (age>=21 and gender.upper()=='MALE'):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def Percentage():
        Subject1=int(input("Subject1="))
        Subject2=int(input("Subject2="))
        Subject3=int(input("Subject3="))
        Subject4=int(input("Subject4="))
        Subject5=int(input("Subject5="))
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total: " ,Total) 
        Percentage=Total/5
        print("Percentage: ", Percentage)
        
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        area=(height*breadth)/2
        print("Area of Triangle: ",area)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth1=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ", height1+height2+breadth1)
        
        
        
        
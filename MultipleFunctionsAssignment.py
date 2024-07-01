# Create a class and function, and list out the items in the list
class SubfieldsInAI:
    def Subfields(str):
        if(str == "AI"):
            SubfieldsAI = ["Machine Learning","Neural Networks", "Vision", "Robotics", 
                           "Speech Processing", "Natural Language Processing"]
            for field in SubfieldsAI:
                print(field)

# Create a function that checks whether the given number is Odd or Even
class OddEven():
    def OddEven():
        num = int(input("Enter the number"))
        if((num%2)==1):
            print(num, "is an Odd Number")
            message = "Odd Number"
        else:
            print(num, "is an Even Number")
            message = "Even Number"
            return message

# Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
class ElegiblityForMarriage():
    def Eligible(strGender, intAge):
        print("Your Gender:",strGender)
        print("Your Age:",intAge) 
        
        if(strGender=="Male"):            
            if(intAge < 21):
                print("NOT ELIGIBLE")
                message = "NOT ELIGIBLE"
            else:
                print("ELIGIBLE")
                message = "ELIGIBLE"
                
        elif(strGender=="Female"):
                if(intAge < 18):
                    print("NOT ELIGIBLE")
                    message = "NOT ELIGIBLE"
                else:
                    print("ELIGIBLE")
                    message = "ELIGIBLE"
        return message

class FindPercent():
    def Percentage():
        intSub1 = int(input("Subject 1"))
        intSub2 = int(input("Subject 2"))
        intSub3 = int(input("Subject 3"))
        intSub4 = int(input("Subject 4"))
        intSub5 = int(input("Subject 5"))
        Total = intSub1 + intSub2 + intSub3 + intSub4 + intSub5
        percentage = Total / 5
        print("Your Total : ", Total)
        print("Your Percentage : ", percentage)
        return percentage

#print area and perimeter of triangle using class and functions
class triangle():
    def Triangle():
        Height = int(input("Height : "))
        Breadth = int(input("Breadth : "))
        Area = (Height*Breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ", Area)
        Height1 = int(input("Height1 : "))
        Height2 = int(input("Height2 : "))
        Breadth1 = int(input("Breadth : "))
        Perimeter = Height1+Height2+Breadth1
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", Perimeter)

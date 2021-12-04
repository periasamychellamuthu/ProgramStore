if __name__=="__main__":
    while(True):
        x= int(input("Enter the year"))
        if x==-1:
            break
        else:
            if (x%400)==0:
                print("Leap Year")
            elif (x%100)==0:
                print("Non Leap Year")
            elif (x%4)==0:
                print("Leap Year")
            else:
                print("Non Leap Year")
#userinput table 
'''pythona=input("Enter a number: ")
a=int(a)
for i in range(1,11):
    print(a,"x",i,"=",a*i) '''
    
    #nested for loop
rows=int(input("enter the  no.of row:"))
cols=int(input("enter the no.of cols:"))
symbol=input("enter the symbol:")
for i in range(rows):
        for j in range(cols):
            print(symbol,end="")
        print()    

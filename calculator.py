while True:
 print("1.Addition")
 print("2.Subtraction")
 print("3.Multiplication")
 print("4.Division")
 print("5.Exit")

 choice =int(input("enter the number :"))

 if choice==1 :
     first_number = int(input("enter the first number :"))
     second_number = int(input("enter the second number :"))
     print(first_number + second_number)

 elif choice==2:
        first_number = int(input("enter the first number :"))
        second_number = int(input("enter the second number :"))
        print(first_number - second_number)
     
     
 elif choice==3:
    
         first_number = int(input("enter the first number :"))
         second_number = int(input("enter the second number :"))
         print(first_number * second_number)
 elif choice==4:
        first_number = int(input("enter the first number :"))
        second_number = int(input("enter the second number :"))
    
        if second_number == 0:
            print("Cannot divide by zero")
        else:
             print(first_number/second_number)
 elif choice==5:
          print("Exiting...")
          break
              
 else:
     print("Invalid choice")
   
             
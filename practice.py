marks = [22,44,55,66,77]
mark=[]
while True:
    print("1.Add marks")
    print("2.View marks")
    print("3.highest marks")
    print("4.average marks")
    print("5.exist")
    
    choice = input("Enter your choice:")
    if choice == "1":
     m=int(input("enter marks"))
     marks.append(m)
     print(marks)
    elif choice == "2":
     for mark in marks:
         print(mark)
    elif choice == "3":
       if len(marks) == 0:
           print("No data")
       else:
           print(max(marks))
    elif choice == "4":
        if len(marks) == 0:
            print("No data")
        else:
            avg = sum(marks)/len(marks)
            print(avg)
    elif choice == "5":
        print("Good bye")        
        break
    else:
        print("Invaild choice")
 

    
    



    

studentname="ERTUGRUL SAMET"

i=3
for x in range(3):
 name=(input("Enter Your Name:\n")).upper()
 
 if name == studentname: 
   x=0
   break

 else:
   i-=1
   print("You Entered User Information Wrong! Please Try Again.\n")
   print("You've {} attempts left\n".format(i))
   x=1


if x==1:
   print("Your System Has Been Temporarily Blocked. Please Try Again Later.\n")

else:
  print("Welcome {}".format(name))
  print("Please Enter 5 Courses:\n")
  lessons=[]
  for x in range(5):
    lessons.append(input("{} Enter The Name Of The Lesson:\n".format(x+1)))
  
  sayi=int(input("How Many Lessons You'll Take:\n"))

  if sayi<3 or sayi>5:
    ok=False
    while(ok !=True):
      sayi=int(input("You've Chosen An Invalid Number Of Courses, Please Re-Enter."))
      ok=(sayi>=3) and (sayi<=5)
  
  if sayi>=3 and sayi<=5:
     print("Please Enter The Courses You'll Take:")
     ders=[]
     for x in range(0,sayi):
       i=input()
       for x in range(0,5):
          if i==lessons[x]:
            ders.append(i)
            lessons[x]="Course Selected."
            test=0
            break
          else:
            test=1
            continue
        

       if test==1:
          
          while test!=0:
             print("You Entered An Invalid Course! Please Choose From The Courses Listed.")
             print("{}".format(lessons[0:5]))
             i=input()
             for x in range(0,5):
               if i==lessons[x]:
                 ders.append(i)
                 lessons[x]="Course Selected."
                 test=0
                 break
              
               else:
                 test=1
  print("The Courses You Choose Are:\n")          
  print(ders[0:sayi])
  secilenders=input("Enter The Course For Which You'll Enter The Grades:")
  for x in range(0,sayi):
    if secilenders==ders[x]:
      dene=1
      break
      
    else:
     dene=0
  
  if dene==0:
       while(dene!=1):
          print("You Entered An Invalid Course:\n")
          secilenders=input("Enter The Course For Which You'll Enter The Grades:\n")
          for x in range(0,sayi):
            if secilenders==ders[x]:
              dene=1
              break
      
            else:
             dene=0
  
  vize=int(input("Enter The Visa Grade Of The {} Course:\n".format(secilenders)))
  final=int(input("Enter The Final Grade Of The {} Course:\n".format(secilenders)))
  proje=int(input("Enter The Project Grade Of The {} Course:\n".format(secilenders)))
      
  sınav={'The Visa': vize, 'The Final': final, 'The Project': proje}
  print(sınav)

  ort=((vize*30)/100)+((final*50)/100)+((proje*20)/100)

  if ort>90:
     print("Your Grade {}\nYou passed with AA.".format(ort))
  elif 70<ort<=90:
     print("Your Grade {}\nYou passed with BB.".format(ort))
  elif 50<ort<=70:
     print("Your Grade {}\nYou passed with CC.".format(ort))
  elif 30<ort<=50:
     print("Your Grade {}\nYou passed with DD.".format(ort))
  elif ort<=30:
     print("Your Grade {}\nYou Failed with FF.\n{} You Failed The Lesson. Take The Lesson Again.".format(ort,secilenders))

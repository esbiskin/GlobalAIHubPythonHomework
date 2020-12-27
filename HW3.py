import random
 
print("THE HANGMAN GAME")

words = ["banana", "corona", "snake", "pineapple", "car", "phone", "book", "dog", "camera", "awesome", "light", "radioactive"]
randomword = random.choice(words)
x = (len(randomword))
z = list('_' * x)
harfler =  []
tahmin_hakki = ()

while True:
  name = input('\n'"Please enter your name: ")
  if len(name) == 0:
    print("You've to enter a name.")
  else:
    break

print('\n'"WELCOME",name.upper())
while True:
  zorluk = input('\n'"Select the difficulty level (easy / hard): ")
  if zorluk.lower() == 'easy':
    tahmin_hakki = 10
    break
  elif zorluk.lower() == 'hard':
    tahmin_hakki = 3
    break
  else:
    print("Please enter a valid option.")
print("You've {} wrong right(s).".format(tahmin_hakki))

#guess
while tahmin_hakki>0:
  guess = input('\n'"Guess a character: ").lower()
  if guess in harfler:
    print("You've entered this letter before.")
  
  elif len(guess) >1 :
    print("Please enter just a letter.")
    continue
  
  elif len(guess) <1:
    print("Please enter a letter.")
    continue

  elif guess not in randomword:
    tahmin_hakki -= 1
    print("Sorry, this letter isn't in the word.",'\n'+'\n'"You've {} wrong right(s).".format(tahmin_hakki))
    harfler.append(guess)

  else:
    for i in range(len(randomword)):
      if guess == randomword[i]:
        z[i] = guess
        harfler.append(guess)
    print("Yippee! True guess!")    
    print( '\n',' '.join(z), end='\n')

  while True: 
    eorh=input('\n'"Would you like to guess (Y/N)? ").lower()
    if eorh == 'y':
      break
    elif eorh == 'n':
      break
    else:
      print("Please enter a valid option.")

  #correct answer loop
  while True:
    if eorh == "y":
      e = input('\n'"Your guess: ").lower()
      if tahmin_hakki == 0:
        break
      if e == randomword:
        print('\n'"WOW! You won!")
        tahmin_hakki = -1
        break 
      else:
        tahmin_hakki -= 1
        print("Oops... You couldn't know.",'\n'+'\n' "You've {} wrong right(s)".format(tahmin_hakki))
        break
    elif eorh == 'n':
     break
    else:
      print("Please enter a true selection.")

  if tahmin_hakki == 0:
    print("Sorry your guesswork ran out.",'\n'+'\n'"Game Over...")
    break

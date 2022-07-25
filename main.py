import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Wybieranie z listy losowej pozycji przez komputer
map=[rock,paper,scissors]
dlugosc_mapy=len(map)
los_komp=random.randint(0,dlugosc_mapy-1)
wybrana_komp=map[los_komp]



#Wybieranie z listy  pozycji przez gracza
gracz=int(input("Podaj liczbe "))
wybrana_gracz=map[gracz]


wygrany=""

#kamien--------------------------------------
if wybrana_gracz==rock:
  print(wybrana_gracz)
  if wybrana_komp==rock:
    print("Komputer wybrał:\n", wybrana_komp)
    wygrany="Remis"
  #papier
  elif wybrana_komp==paper:
    print("Komputer wybrał:\n", wybrana_komp)
    wygrany="Komputer"
  #nożycze
  elif wybrana_komp==scissors:
    print("Komputer wybrał:\n", wybrana_komp)
    wygrany="Gracz"



#papier--------------------------------------
elif wybrana_gracz==paper:
  print(wybrana_gracz)
  if wybrana_komp==paper:
    print("Komputer wybrał:\n", wybrana_komp)
    wygrany="Remis"
  #papier
  elif wybrana_komp==rock:
    print("Komputer wybrał:\n", wybrana_komp)
    wygrany="Gracz"
  #nożycze
  elif wybrana_komp==scissors:
    print("Komputer wybrał:\n", wybrana_komp)
    wygrany="Komputer"



#nozyce--------------------------------------
elif wybrana_gracz==scissors:
  print(wybrana_gracz)
  if wybrana_komp==scissors:
    print("Komputer wybrał:\n", wybrana_komp)
    wygrany="Remis"
  #papier
  elif wybrana_komp==rock:
    print("Komputer wybrał:\n", wybrana_komp)
    wygrany="Komputer"
  #nożycze
  elif wybrana_komp==paper:
    print("Komputer wybrał:\n", wybrana_komp)
    wygrany="Gracz"


print("Wygrał:", wygrany)

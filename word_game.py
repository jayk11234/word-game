from itertools import permutations
from random import choice , sample
from string import ascii_lowercase
import pygame,time
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('C:\\Users\jyoti\Music\mixkit-melodic-bonus-collect-1938.wav')
pygame.mixer.music.play()
#--------------------------------------------------------------------------------------------------------------------
""" first_filter takes three arguments (string,list one, list two) and appends all words in list one where
length of a word in list two is >2 but <len(string), it returns None"""    
def first_filter(word,wlist,w1list): 
    missingletters = set(ascii_lowercase)-set(x for x in word)
    
    o_w = len(word)
    for line in w1list:
        check_pass = 1
        line = line.rstrip('\n')
        if len(line) <= o_w and len(line) > 2:
            for x in line:
             if x in missingletters:
               check_pass = 0
               break 
            if check_pass:
              wlist.append(line)     


""" second_filter takes 4 arguments(string,list one,list two,len of list two), and uses binary search to find if the
string is present in list two and if present appends it to list one, it return None"""
def second_filter(item,list1,wlist,n):
  beg=0
  end = n-1
  while beg<=end:
    mid = (beg+end)//2
    if wlist[mid] < item:
      beg = mid + 1

    elif wlist[mid] > item:
      end = mid - 1

    elif wlist[mid] == item:
      list1.append(item)
      break    

#--------------------------------------------------------------------------------------------------------------------
#formatted_dict.txt contains all words which have 3 <= len(word)<= 8
#fr is a file object that we created to read the file
fr = open('formatted_dict.txt')
#readlines() method works on fr and returns a list in which each line of the file is stored  as a string element
#where the string ends with '\n'
w1list = fr.readlines()      

#variable for storing choice entered by user in the while loop
ch ='c'
#--------------------------------------------------------------------------------------------------------------------
print('')
print('''
BREIF INTRODUCTION OF GAME:-\n
1.In this game,player will be given any random word(obviously an english word).\n
2.The player then has to create their own word from the alphabets given in the word in front of them.\n
3.If their word is an existing english word only then they will be awarded points.\n
4.They will given 3 tries to input their own words.\n
5.Else if player inputs a word which contains any letter that was not given in the word provided to them then they don't get any points.\n
7.After three tries total points gained by player will be displayed to them.\n
''')
time.sleep(1)

print('\nDo you want to start the game? ')
print('\nPress Y ---------> To play')
print('\nPress N ---------> To exit')
start_game = input()

if start_game == 'y' or start_game == 'Y':

  #game loop starts here
  #\\\\\\\\ variable --------> word below is referred to as --------> 'word'\\\\\\\\\
  while True:
   #choice 1 -------> continue playing game 
   if ch == 'c' or ch == 'C':
     #while loop to find a word such that len('word') > 6 , if such a word is found then a wlist is created with all
     #words that are the same length as 'word' and also only has alphabets that are in 'word' and also has more than
     #10 different combinations  exiting in engish made from its contituent alphabets
     while True:
       #chooses a random word
       #strip removes '\n' from the end of the string bcs when it is selected from w1list it still has '\n'
       word = choice(w1list).strip('\n')
       #checks if len('word') > 6 
       if len(word) > 6:
         #makes a wlist if len('word') > 6
         wlist = []
         first_filter(word,wlist,w1list)
         n = len(wlist)
         #create list1 to store all possible combinations of constituent alphabets of 'word' that make legit english
         #words
         list1 = []
         #for loop to create all possible combinatins of 'word'
         #starts with 3 bcs we want min word length to be 3 and max word length can be len('word')
         for i in range(3,len(word)+1):
           #creates all combinations of 'word' and stores it in p
           #syntax of permuations --->permuations('word whose letters you wanna use,len of the resulting combination')
           p = permutations(word,i)
           # i is a tuple
           for i in p:
                item = ''.join(i)
                #call function second_filter to check legitness
                second_filter(item,list1,wlist,n)
                
         #checks if there are more than 10 different words in list1
         #here (set) is used which stores only one copy of each element unlike a (list)
         list1_set = set(x for x in list1)       
         if len(list1_set)> 10:
           break
     #stores lenght of the smallest word
     list1_min = min(len(x) for x in list1_set)
     #stores length of the longest word
     list1_max = max(len(x) for x in list1_set)
     
     #print(list1_set)
     #jumbles the letters in 'word'
     word1 = "".join(sample(word,len(word)))
     time.sleep(2)
##     pygame.mixer.music.load('‪‪soundtyping.wav')
##     pygame.mixer.music.play()
     #prints 'word'
     print('\nYour word is:\n')
     time.sleep(1)
     word1 = word1.upper()
     for c in word1:
       pygame.mixer.music.load('soundtyping.wav')
       pygame.mixer.music.play()  
       print(c,end='')
       time.sleep(0.5)
     pygame.mixer.music.unload()  
       
     #score to keep track of score of user
     score = 0  
     #for loop to input from user 3 times
     #list to store the words entered by user in each try
     trylist = []
     for i in range(1,4):
          
          time.sleep(1)
          print('\n\nTry',i)
          time.sleep(1)

          userw = input('\nYour word:')
          if userw in trylist:
              time.sleep(0.5)
              print('\nWord already entered!!')
              time.sleep(0.5)
              pygame.mixer.music.load('wrong ans.wav')
              pygame.mixer.music.play()
              print("\nYou don't earn any points :/")
              pygame.mixer.music.unload()
          else:
            trylist.append(userw)  
            u_len = len(userw)
            #if user inputs a legit english word then points are given 
            if userw in list1_set:
              #if the smalles word that can be made has been inputted then 10 points are given
              if u_len == list1_min:
                time.sleep(0.5)
                pygame.mixer.music.load('small_win.wav')
                pygame.mixer.music.play()
                print('\nYay you earn 10 points!!')
                score+=10
              #if the largest word that can be made has been inputted then 100 points are given  
              elif u_len == list1_max:
                time.sleep(0.5)
                pygame.mixer.music.load('winning.mp3')
                pygame.mixer.music.play()
                print('\nYay you earn 100 points!!')
                score+=100
              #any other length word is given 50 points
              else:
                score+=50
                time.sleep(0.5)
                pygame.mixer.music.load('small_win.wav')
                pygame.mixer.music.play()
                print("\nYay you earn 50 points!!")
            #if legit word is not inputtted then user gets no point   
            elif userw not in list1_set or userw =='':
              time.sleep(0.5)
              #pygame.mixer.music.load('‪‪‪wrong ans.wav')
              #pygame.mixer.music.play()
              print("\nYou don't earn any points :/")
     #options to either continue or exit game
     time.sleep(2)
     #pygame.mixer.music.play()
     print('\nTotal score: ',score)
     print('The original word is: ',word.upper())
     print('\nPress C ------> To continue playing')
     print('\nPress E ------> To exit')
     time.sleep(0.25)
     ch = input()
    
   elif ch == 'e' or ch == 'E':
       exit()
   else:
       print('\n \\Wrong choice, Pls choose from the given choices\\')
       ch = input()
else:
  exit()
#end of program------------------------------------------------------------------------------------------------------  
          

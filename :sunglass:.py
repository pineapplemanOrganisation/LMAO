import random
import string
import pyautogui
ch = ' a b c d e f g h i j k l m n o p q r s t u v w x y z '

ch_list = list(ch)

password = pyautogui.password("set your password: ")

guess_p = ""
while (guess_p != password):
   guess_p = random.choices(ch_list, k=len(password))
    print("==========" + str(guess_p) + "==========")
    if (guess_p==password):
      print("password is : " + "" .join(guess_p))
      break
    

import random
def word_selection():
   i = 0
   linenum = random.randint(0, 267751)
   with open('sowpods.txt', 'r') as f:
      line = f.readline()
      while line:
         line = f.readline()
         i+=1
         if i == linenum:
            break
   f.close()
   return line
def main():
   print("Welcome to Hangman!")
   retry = "y"
   while retry == "y":
      word = word_selection()
      tries = 6
      guess = [' _ ']*(len(word) -1)
      num_remain = len(word)
      print(guess)
      while tries != 0:
         ch = input("Choose a character\n")
         ch = ch.upper()
         num_changes = 0
         for i in range(len(word)):
            if word[i] == ch:
               guess[i] = ch
               num_changes += 1
         if num_changes == 0:
            tries -= 1
         num_changes = 0
         print(guess)
         if num_remain == 0:
            print("You win!")
            break
         elif tries == 0:
            print("You lose")
            print(word)
      retry = input("Press 'y' to play again!\n")
      if retry != "y":
         break      
         
if __name__=="__main__":
   main()      

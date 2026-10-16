# ------------------------------------------------------
#        Name: Yoyo Zheng
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Add your docstring """
    
import sys

secret_word = "food"

# Task 1
def check_text():
    """Prompts for input until secret_word or dog/Dog is entered."""
    
    #repeats like a loop
    while True:
        user_input = input("Give me a sentence:") #Ask for user to input a sentence
        words = user_input.split() #Split the user input into words and then storing them into the variable "words" 

        found_secret = False
        found_dog = False

        for word in words:
            
            #if any of the word stored in the variable "words" equals to the "secret word" or "dog", then the statement turns into true
            if word == secret_word or word == secret_word.capitalize():
                found_secret = True
                break
            if word == "dog" or word == "Dog" or word == "dogs" or word == "Dogs":
                found_dog = True
                break
            
        #As the statement turns into true, print a string
        if found_secret:
            print("You used the secret word!")
            break
        elif found_dog:
            print('You used the word "dog" or the word "Dog"!')
            break
        
        #if the statement stay false, print a string
        else:
            print("Try again")



# Task 2
def check_greater():
    """ Add your docstring """
    
    while True:
    
        #ask the user to input 2 integers
        first_int = int(input("Give me an integer:"))
        second_int = int(input("Give me an another integer:"))
    
        first_greater = False
        second_greater = False
        
        #if the first integer the user inputed is bigger than the second, than assign Ture to the variable "first_greater"
        if first_int > second_int:
            first_greater = True
        elif first_int < second_int:
            second_greater = True
    
        #when the variable first_greater is True, print "First is Greater"
        if first_greater:
            print("First is Greater")
            break
        
        elif second_greater:
            print("Second is Greater")
            break
            
        #except the 2 situations listed above, print "Try again"
        else:
            print("Try again")
            


# Task 3
def get_special_numbers():
    """ Add your docstring """
    
    for num in range(1, 40):
        
        #if the remainder of num divided by 2 is 0, then the number is skipped
        if num % 2 == 0:
            continue
        
        #if the remainder of num divided by 3 does not equal to 0, then the number is skipped
        if num % 3 != 0:
            continue
        
        #if the remainder of num divided by 5 is 0, then the number is skipped
        if num % 5 == 0:
            continue
        
        else:
            print(num)


# Task 4.a
def my_for_loop():
    """ Add your docstring """
    
    #ask for user to input a word
    word = input("Give me a word: ")
    
    #check the length of the user input
    if len(word) < 2 or len(word) > 5:
        print("bad word")
        return
    
    #check if there is space in the user input
    if " " in word:
        print("bad word")
        return
    
    for char in word:
        if char.lower() in "aeiou":
            print(f"{char} is a vowel")
        else:
            print(f"{char} is a consonant")

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    
    while True:
        choice = input("Give me a letter: ")
        
        if choice == "a":
            continue
        elif choice == "b":
            print("Goodbye")
            return
        elif choice == "c":
            sys.exit()
        else:
            print("try again")

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")

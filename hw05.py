"""
Name: (Helena Brieske)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """ This function lets you ask for a letter as input from the user. If the input is not a single character, the user will be informed of this. If the input is a single character however and if the letter is A, B or C, then the input will be returned, else a message will inform the user that they provided the wrong character """
    #ask for input
    #need nested loops with if, elif, else
    #if length wrong, print error and continue
    #if not a,b,c print error, if a, b, c return
    while True:
        letter = input("Give an single uppercase letter: ")
        length = len(letter)
        if length != 1:
            print("Error: it needs to be a single character.")
            continue
        elif length == 1:
            if letter == "A" or letter == "B" or letter == "C":
                return letter
            else:
                print("Error: You provided the wrong character.")
                continue
            
    
    

def get_digit():
    """ This function asks for a single number character and if the input is not a digit, then the user will be informed of this and the loop will be restarted. If it is a single digit that is not between 1-3 inclusive, then the user will also be informed of this. If the input is 1,2 or 3, then the character will be returned. """
    #ask for input
    #if wrong print error and continue
    #if not 1,2,3 print error and continue
    #if 1,2,3 return character
    while True:
        digit = (input("Give me an single number character: "))
        if digit.isdigit() == False:
            print("Error: your input should be only digits.")
            continue
        elif digit != "1" and digit != "2" and digit != "3":
            print("Error: a single digit needs to be in [1,3].")
            continue
        elif digit == "1" or digit == "2" or digit == "3":
            return (digit)
    

def check_pattern(letter, digit, st_list):
    """ This function receives the letter character and the digit character the string character called st_list as input. Check_pattern then checks if any of the words inside the list contain the letter and number (in that order) and prints any that do contain them """
    #st_list serves as input for the check_pattern function
    #check if any of these words inside the list contain the letter and number (in this order)
    #if so, print once
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]
    print("Strings with the pattern:")
    for elem in st_list:
        pos = len(elem)
        for i in range(len(elem)):
            if (letter == elem[i]):
                pos = i
                break
        for i in range(pos+1, len(elem)):
            if (digit == elem[i]):
                print(f"{elem}", end=" ")
                break


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""
    
    
    
    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]
    
    
    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    #make loop that does these things until last step leads to break
    #get letter and digit
    #check pattern and print
    #ask try again y/n
    #if response not y, it ends
    while True:
        letter = get_letter()
        print(f"{letter}")
        digit = get_digit()
        print(f"{digit}")
        check_pattern(letter, digit, st_list)
        answer = input("\nTry Again? (y/n):")
        if (answer == "y"):
            continue
        else:
            break
   
            
    
        

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()
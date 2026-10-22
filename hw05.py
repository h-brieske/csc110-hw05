"""
Name: (Helena Brieske)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """ Add your own Docstring """
    
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
    """ Add your own Docstring """
    while True:
        digit = (input("Give me an single number character: "))
        if digit.isdigit() == False:
            print("Error: your input should be only digits:")
            continue
        elif digit != "1" and digit != "2" and digit != "3":
            print("Error: a single digit needs to be in [1,3].")
            continue
        elif digit == "1" or digit == "2" or digit == "3":
            return (digit)
    

def check_pattern(letter, digit, st_list):
    """ Add your own Docstring """
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]
    for elem in st_list:
        pos = len(elem)
        for i in range(len(elem)):
            if (letter == elem[i]):
                pos = i
                break
        for i in range(pos+1, len(elem)):
            if (digit == elem[i]):
                print(f"{elem}")
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
    while True:
        letter = get_letter()
        print(f"{letter}")
        digit = get_digit()
        print(f"{digit}")
        check_pattern(letter, digit, st_list)
        answer = input("Try Again? (y/n):")
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
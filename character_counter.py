# character_counter.py
# Author: ars3ツ
# Description: A simple Python script that counts the number of characters in a user-inputted string.

def count_characters():
    """
    Prompts the user to enter a string and displays the character count.
    """
    user_input = input("Enter a string: ").strip()
    
    # Count all characters including spaces and punctuation
    num_chars = len(user_input)
    
    print(f"You entered {num_chars} characters.")

if __name__ == "__main__":
    count_characters()

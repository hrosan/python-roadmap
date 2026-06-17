'''
Challenge 2: The Vowel Counter
- Create a reusable function called count_vowels(text: str).
- Inside the function, create a counter variable starting at 0.
- Loop through every letter in the text string (Hint: for letter in text: works perfectly in Python!).
- Use an if statement to check if the letter is in "aeiouAEIOU". If it is, add 1 to the counter.
- If there's an equal vowel don't add it to counter.
- The function should return the final count.
- Test it by calling the function with a few different words and printing the result.
'''

# INITIALIZE FUNCTION
def count_vowels(text: str) -> int:
    # Initialize local variables
    vowels: str = "aeiouAEIOU" # All vowels used in portuguese and English
    vowel_counter: int = 0 # It starts from zero

    if isinstance(text, str): # Validate the datatype coming from the user/program | Returns True if text were a string
        # Looping through the words to count every vowel
        for letter in text: # Loop through  the text
            if letter in vowels: # Verify if the char is a string
                vowel_counter += 1 # If the statement were true, increase counter
        # Returning the result to the user
        return vowel_counter
    
    else:
        raise TypeError # Raise an error about the datatype to user

# INITIALIZING THE TEST
phrase_1 = "Python is awesome"
phrase_2 = "AaEeIiOoUu"
phrase_3 = "Rhythm rhythms! 1234"
phrase_4 = "The quick brown fox jumps over the lazy dog."

test1 = count_vowels(phrase_1)
print(test1)
test2 = count_vowels(phrase_2)
print(test2)
test3 = count_vowels(phrase_3)
print(test3)
test4 = count_vowels(phrase_4)
print(test4)
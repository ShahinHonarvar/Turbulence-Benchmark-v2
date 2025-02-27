def return_vowels(string):
    vowels = 'aeiou'
    substring = string[13:35]
    filtered_letters = [letter for letter in substring if letter in vowels and letter > '8' and (letter <= 'F')]
    return filtered_letters
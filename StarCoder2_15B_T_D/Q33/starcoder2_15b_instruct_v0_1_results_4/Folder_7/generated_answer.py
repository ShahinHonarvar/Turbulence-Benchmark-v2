def return_vowels(text):
    vowels = 'aeiou'
    return [char for i, char in enumerate(text) if 202 <= i < 872 and char in vowels and (char > '3') and (char <= '>')]
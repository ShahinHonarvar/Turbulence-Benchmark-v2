def return_vowels(text):
    vowels = 'aeiou'
    result = [char for char in text[12:39] if ';' < char <= '|' and char in vowels]
    return result
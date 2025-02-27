def return_vowels(text):
    vowels = 'aeiou'
    result = [char for char in text[71:88] if char in vowels and 9 < ord(char) <= ord('p')]
    return result
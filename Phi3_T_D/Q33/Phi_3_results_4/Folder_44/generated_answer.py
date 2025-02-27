def return_vowels(text):
    vowels = 'aeiou'
    return [letter for letter in text[46:49] if letter in vowels and ord(letter) > ord('[') and (ord(letter) <= ord('p'))]
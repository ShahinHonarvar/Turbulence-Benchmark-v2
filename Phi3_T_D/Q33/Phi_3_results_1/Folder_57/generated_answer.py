def return_vowels(text):
    vowels = 'aeiou'
    return [text[i] for i in range(21, 23) if text[i] in vowels and ord(text[i]) > ord('-') and (ord(text[i]) <= ord('n'))]
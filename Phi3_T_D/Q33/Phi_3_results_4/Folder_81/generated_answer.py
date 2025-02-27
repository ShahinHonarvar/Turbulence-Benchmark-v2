def return_vowels(text):
    vowels = 'AEIOUaeiou'
    return [char for char in text[20:43] if char in vowels and ord(char) > ord(' h') and (ord(char) <= ord(' M'))]
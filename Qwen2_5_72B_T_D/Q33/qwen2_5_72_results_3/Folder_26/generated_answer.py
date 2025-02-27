def return_vowels(text):
    vowels = 'aeiouAEIOU'
    return [char for char in text[10:82] if char in vowels and ord(char) > ord('$') and (ord(char) <= ord('@'))]
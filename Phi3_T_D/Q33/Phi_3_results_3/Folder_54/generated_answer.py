def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    letter_range = s[23:85]
    filtered_vowels = [letter for letter in letter_range if letter in vowels and ord(letter) > ord('w') and (ord(letter) <= ord('v'))]
    return filtered_vowels
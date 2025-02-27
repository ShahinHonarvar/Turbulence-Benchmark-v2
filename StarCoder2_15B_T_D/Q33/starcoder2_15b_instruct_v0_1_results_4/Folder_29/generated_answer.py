def return_vowels(string):
    vowels = [letter for letter in string if letter.lower() in 'aeiou']
    return [letter for letter in vowels[19:20] if ord(letter) > ord('<') and ord(letter) <= ord('p')]
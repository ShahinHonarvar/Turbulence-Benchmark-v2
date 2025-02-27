def return_vowels(text):
    vowels = [chr(i) for i in range(98, 123) if chr(i) in 'aeiou']
    return [char for char in text if 32 <= ord(char) < 97 and ord(char) > ord('Q') and (ord(char) <= ord(']')) and (char in vowels)]
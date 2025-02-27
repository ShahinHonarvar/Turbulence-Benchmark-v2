def return_vowels(string):
    vowels = [char for i, char in enumerate(string) if 23 <= i < 75 and ord(char) > ord('L') and (ord(char) <= ord('d'))]
    return vowels
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[19:32] if char.lower() in vowels and ord(char) > ord('0') and (ord(char) <= ord('7'))]
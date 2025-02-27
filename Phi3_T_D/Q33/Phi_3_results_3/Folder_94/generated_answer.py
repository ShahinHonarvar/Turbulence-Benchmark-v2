def return_vowels(s):
    if len(s) < 94:
        return []
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[40:94] if char in vowels and ord(char) > ord('5') and (ord(char) <= ord('H'))]
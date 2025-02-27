def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[23:57] if char > '0' and char <= 'd' and (char in vowels)]
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[37:57] if char > '*' and char <= 'P' and (char in vowels)]
    return result
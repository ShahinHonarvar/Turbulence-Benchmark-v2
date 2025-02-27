def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[13:37] if 'Z' < char <= '}' and char in vowels]
    return result
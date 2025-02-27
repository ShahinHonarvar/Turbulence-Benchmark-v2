def return_vowels(s):
    start = 70
    end = 76
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[start:end] if char.lower() in vowels and char.lower() > 'c']
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[495:837] if char in vowels and 'b' < char <= 't']
    return result
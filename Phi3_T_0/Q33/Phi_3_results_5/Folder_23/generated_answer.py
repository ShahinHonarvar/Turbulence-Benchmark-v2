def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[56:96] if char in vowels and '&' < char <= 'T']
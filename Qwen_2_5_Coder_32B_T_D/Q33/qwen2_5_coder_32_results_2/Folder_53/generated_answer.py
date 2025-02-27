def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[27:57] if char in vowels and 'o' < char <= 'w']
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[3:9] if char in vowels and 's' < char <= 'u']
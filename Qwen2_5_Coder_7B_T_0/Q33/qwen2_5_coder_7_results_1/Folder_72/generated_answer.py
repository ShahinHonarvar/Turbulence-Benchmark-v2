def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[37:57] if char in vowels and '*' < char <= 'P']
    return result
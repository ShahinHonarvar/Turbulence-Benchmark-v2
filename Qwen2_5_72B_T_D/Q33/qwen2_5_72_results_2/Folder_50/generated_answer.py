def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[11:53] if char in vowels and '+' < char <= 'W']
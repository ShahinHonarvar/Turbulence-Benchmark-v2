def return_vowels(s):
    vowels = [char for char in s[1:5] if char in 'aeiou' and '!' < char <= 'j']
    return vowels
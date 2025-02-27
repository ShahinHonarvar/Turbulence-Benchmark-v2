def return_vowels(s):
    vowels = [char for char in s[604:949] if char in 'AEIOU' and 'N' < char <= 'U']
    return vowels
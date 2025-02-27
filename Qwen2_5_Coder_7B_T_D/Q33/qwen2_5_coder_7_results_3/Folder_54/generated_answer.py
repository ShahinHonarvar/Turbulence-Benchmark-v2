def return_vowels(s):
    vowels = [char for i, char in enumerate(s[23:85]) if char in 'aeiou' and 'W' < char <= 'v']
    return vowels
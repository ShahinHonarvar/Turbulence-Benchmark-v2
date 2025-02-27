def return_vowels(s):
    vowels = [char for char in s[529:828] if char in 'aeiou' and 'U' < char <= 'l']
    return vowels
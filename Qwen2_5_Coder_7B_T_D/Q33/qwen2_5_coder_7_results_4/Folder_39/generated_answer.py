def return_vowels(s):
    vowels = [char for char in s[32:97] if char in 'aeiou' and 'Q' < char <= ']']
    return vowels
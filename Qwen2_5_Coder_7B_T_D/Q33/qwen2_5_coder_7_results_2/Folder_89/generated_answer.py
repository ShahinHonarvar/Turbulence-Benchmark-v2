def return_vowels(s):
    vowels = [char for char in s[50:51] if char in 'aeiou' and char > ',' and (char <= 'v')]
    return vowels
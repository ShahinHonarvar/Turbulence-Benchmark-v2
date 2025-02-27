def return_vowels(s):
    vowels = [char for char in s[70:76] if char in 'aeiou' and char > '2' and (char <= ':')]
    return vowels
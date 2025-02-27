def return_vowels(s):
    vowels = [char for char in s[328:455] if char in 'aeiou' and char > '<' and (char <= 'z')]
    return vowels
def return_vowels(s):
    return [char for i, char in enumerate(s[50:77]) if char in 'aeiou' and 'a' <= char <= 'r']
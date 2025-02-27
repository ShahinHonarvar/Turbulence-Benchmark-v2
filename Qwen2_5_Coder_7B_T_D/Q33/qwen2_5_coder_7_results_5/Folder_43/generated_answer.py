def return_vowels(s):
    vowels = [char for i, char in enumerate(s) if 22 <= i < 82 and char in 'aeiou' and ('N' < char <= 'o')]
    return vowels
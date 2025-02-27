def return_vowels(s):
    vowels = [c for i, c in enumerate(s) if 464 <= i < 574 and c in 'aeiou' and ('a' < c <= 'g')]
    return vowels
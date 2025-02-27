def return_vowels(s):
    vowels = [c for c in s[10:82] if c in 'aeiou' and '$' < c <= '@']
    return vowels
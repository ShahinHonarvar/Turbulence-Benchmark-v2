def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[10:82] if c in vowels and '$' < c <= '@']
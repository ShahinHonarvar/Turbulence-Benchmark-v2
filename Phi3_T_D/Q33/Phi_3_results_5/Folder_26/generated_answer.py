def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = [char for char in s[10:82] if char in vowels and '$' < char <= '@']
    return result
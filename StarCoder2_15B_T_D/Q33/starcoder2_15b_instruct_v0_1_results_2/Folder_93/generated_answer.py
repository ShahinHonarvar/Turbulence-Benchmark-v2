def return_vowels(string):
    substring = string[54:82]
    vowels = [char for char in substring if char in 'aeiou']
    filtered_vowels = [vowel for vowel in vowels if vowel > '=' and vowel <= '@']
    return filtered_vowels
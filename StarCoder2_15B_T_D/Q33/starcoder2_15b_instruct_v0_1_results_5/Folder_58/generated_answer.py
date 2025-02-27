def return_vowels(string):
    vowels = 'aeiou'
    vowels_in_range = [vowel for vowel in vowels if vowel > '%' and vowel <= 'U']
    return vowels_in_range
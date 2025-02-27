def return_vowels(string):
    vowels = 'aeiou'
    return [c for i, c in enumerate(string) if 20 <= i < 34 and c in vowels and ('u' < c <= 'i')]
def return_vowels(string):
    vowels = 'aeiou'
    return [c for i, c in enumerate(string) if 34 <= i < 58 and c in vowels and ('b' < c <= 'o')]
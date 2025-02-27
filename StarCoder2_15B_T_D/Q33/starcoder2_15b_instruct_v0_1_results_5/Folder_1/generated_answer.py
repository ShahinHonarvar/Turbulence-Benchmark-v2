def return_vowels(string):
    vowels = 'aeiou'
    return [c for i, c in enumerate(string) if 24 <= i < 64 and c in vowels and ('f' < c <= 'h')]
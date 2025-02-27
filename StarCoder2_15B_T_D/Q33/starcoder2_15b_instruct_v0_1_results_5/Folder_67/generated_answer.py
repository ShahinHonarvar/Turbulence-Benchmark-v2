def return_vowels(string):
    vowels = 'aeiou'
    return [c for i, c in enumerate(string) if 21 <= i < 59 and c in vowels and (c > '/') and (c <= 'a')]
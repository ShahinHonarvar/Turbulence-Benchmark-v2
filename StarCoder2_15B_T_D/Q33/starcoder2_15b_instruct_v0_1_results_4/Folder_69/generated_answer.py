def return_vowels(string):
    vowels = 'aeiou'
    return [c for i, c in enumerate(string) if 641 <= i < 872 and c in vowels and (c > '>') and (c <= 'q')]
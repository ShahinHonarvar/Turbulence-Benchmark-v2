def return_vowels(string):
    vowels = 'aeiou'
    return [c for c in string[27:57] if c in vowels and c > 'o' and (c <= 'w')]
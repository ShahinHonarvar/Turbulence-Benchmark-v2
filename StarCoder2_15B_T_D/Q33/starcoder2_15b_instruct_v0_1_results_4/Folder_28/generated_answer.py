def return_vowels(string):
    vowels = 'AEIOU'
    return [ch for i, ch in enumerate(string) if 41 <= i < 50 and ch in vowels and (ch > 'W') and (ch <= '[')]
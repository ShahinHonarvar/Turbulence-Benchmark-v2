def return_vowels(string):
    vowels = 'aeiou'
    return [char for i, char in enumerate(string) if 14 <= i < 60 and char in vowels and (char > 'd') and (char <= 'v')]
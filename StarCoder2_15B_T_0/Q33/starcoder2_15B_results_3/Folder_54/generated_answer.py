def return_vowels(string):
    vowels = 'aeiou'
    return [char for i, char in enumerate(string) if 23 <= i < 85 and char in vowels and (char > 'W') and (char <= 'v')]
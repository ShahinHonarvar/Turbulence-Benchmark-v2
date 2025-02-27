def return_vowels(string):
    vowels = 'aeiou'
    return [char for i, char in enumerate(string) if 23 <= i < 57 and char > '0' and (char <= 'd') and (char in vowels)]
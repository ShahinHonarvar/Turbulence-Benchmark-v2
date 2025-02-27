def return_vowels(string):
    vowels = 'aeiou'
    return [char for i, char in enumerate(string) if i >= 19 and i < 20 and (char > '<') and (char <= 'p') and (char in vowels)]
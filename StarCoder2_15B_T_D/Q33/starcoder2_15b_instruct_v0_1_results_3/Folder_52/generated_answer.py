def return_vowels(string):
    vowels = 'aeiou'
    return [char for i, char in enumerate(string) if i >= 24 and i < 68 and (char in vowels) and (char > 'f') and (char <= '|')]
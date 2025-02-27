def return_vowels(string):
    vowels = 'aeiou'
    return [char for i, char in enumerate(string) if 51 <= i < 77 and char > '4' and (char <= '=') and (char in vowels)]
def return_vowels(string):
    vowels = 'AEIOU'
    return [char for char in string[20:41] if char in vowels and char > 'K' and (char <= 'Z')]
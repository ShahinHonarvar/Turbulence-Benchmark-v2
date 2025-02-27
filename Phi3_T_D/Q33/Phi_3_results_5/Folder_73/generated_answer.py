def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[47:89] if char > '@' and char <= 'n']
    return [char for char in result if char in vowels]
def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[50:51] if char in vowels and char > 'e' and (char <= 'v')]
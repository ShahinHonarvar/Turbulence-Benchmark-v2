def return_vowels(string):
    vowels = 'aeiou'
    filtered_vowels = [char for char in string[260:322] if char in vowels and char > '%' and (char <= 'U')]
    return filtered_vowels
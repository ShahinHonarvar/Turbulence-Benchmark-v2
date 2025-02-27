def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, char in enumerate(string):
        if i >= 77 and i < 84 and char.isalpha() and char.islower():
            if char in vowels and char > 'c' and (char <= 'g'):
                result.append(char)
    return result
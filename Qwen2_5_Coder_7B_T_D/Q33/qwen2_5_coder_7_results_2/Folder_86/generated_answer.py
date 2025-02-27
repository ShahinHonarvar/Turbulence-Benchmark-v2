def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[273:275]:
        if char in vowels and char > '+' and (char <= 'o'):
            result.append(char)
    return result
def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, c in enumerate(string):
        if i >= 19 and i < 32 and (c > '0') and (c <= '7') and (c in vowels):
            result.append(c)
    return result
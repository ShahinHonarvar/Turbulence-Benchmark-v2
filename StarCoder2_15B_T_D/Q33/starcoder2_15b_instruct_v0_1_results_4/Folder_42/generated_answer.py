def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, c in enumerate(string):
        if i >= 12 and i < 39 and (c in vowels) and (';' < c <= '|'):
            result.append(c)
    return result
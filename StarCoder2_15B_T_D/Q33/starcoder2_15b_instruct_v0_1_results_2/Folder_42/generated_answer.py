def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i, c in enumerate(string):
        if 12 <= i < 39 and c in vowels and (';' < c <= '|'):
            result.append(c)
    return result
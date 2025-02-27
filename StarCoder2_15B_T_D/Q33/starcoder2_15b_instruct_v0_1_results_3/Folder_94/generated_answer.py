def return_vowels(text):
    vowels = 'aeiou'
    result = []
    for i, c in enumerate(text):
        if i >= 40 and i < 94 and (c in vowels) and (ord(c) > ord('4')) and (ord(c) <= ord('H')):
            result.append(c)
    return result
def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(56, 68):
        if i < len(string) and string[i] in vowels and ('m' < string[i] <= 'x'):
            result.append(string[i])
    return result
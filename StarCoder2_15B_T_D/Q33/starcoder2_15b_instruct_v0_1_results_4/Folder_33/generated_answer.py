def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(163, 771):
        if i < len(string) and string[i] in vowels and (string[i] > ':') and (string[i] <= 'E'):
            result.append(string[i])
    return result
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, char in enumerate(string):
        if i >= 11 and i < 53 and (char > '+') and (char <= 'W'):
            result.append(char)
    return result
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, char in enumerate(string):
        if i >= 133 and i < 306 and (char in vowels) and (char > 'c') and (char <= 'd'):
            result.append(char)
    return result
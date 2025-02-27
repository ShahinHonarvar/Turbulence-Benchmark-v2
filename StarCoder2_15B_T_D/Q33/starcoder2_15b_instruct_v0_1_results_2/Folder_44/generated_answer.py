def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, char in enumerate(string):
        if i >= 46 and i < 49 and (char in vowels) and (char > '[') and (char <= 'p'):
            result.append(char)
    return result
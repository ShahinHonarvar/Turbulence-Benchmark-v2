def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index, char in enumerate(string):
        if index >= 34 and index < 69 and (char in vowels) and (char > '_') and (char <= 'o'):
            result.append(char)
    return result
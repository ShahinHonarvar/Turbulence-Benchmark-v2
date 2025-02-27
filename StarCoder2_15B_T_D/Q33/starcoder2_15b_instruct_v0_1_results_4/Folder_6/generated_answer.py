def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, char in enumerate(string):
        if i >= 20 and i < 34 and (char.lower() in vowels) and (char.lower() > 'u') and (char.lower() <= 'i'):
            result.append(char)
    return result
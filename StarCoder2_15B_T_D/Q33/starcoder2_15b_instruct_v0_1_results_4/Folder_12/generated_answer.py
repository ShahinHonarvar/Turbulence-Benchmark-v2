def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, char in enumerate(string):
        if i >= 13 and i < 37 and char.isalpha() and (char.lower() in vowels) and (char > 'Z') and (char <= '}'):
            result.append(char)
    return result
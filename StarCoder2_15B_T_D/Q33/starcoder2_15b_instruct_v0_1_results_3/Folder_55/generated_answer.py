def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, char in enumerate(string):
        if char in vowels and 1 <= i < 5 and (char > '!') and (char <= 'j'):
            result.append(char)
    return result
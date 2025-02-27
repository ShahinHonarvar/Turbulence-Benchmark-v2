def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, char in enumerate(string):
        if char in vowels and 328 <= i < 455:
            result.append(char)
    return result
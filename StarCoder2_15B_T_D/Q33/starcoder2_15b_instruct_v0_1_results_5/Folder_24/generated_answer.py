def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index, character in enumerate(string):
        if index >= 23 and index < 57 and (character > '0') and (character <= 'd'):
            if character in vowels:
                result.append(character)
    return result
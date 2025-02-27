def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(23, 38):
        if i < len(string) and string[i] > 'N' and (string[i] <= 'k'):
            result.append(string[i])
    return result
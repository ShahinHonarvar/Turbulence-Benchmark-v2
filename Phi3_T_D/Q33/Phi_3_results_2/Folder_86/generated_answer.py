def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(273, 275):
        if s[i] in vowels and s[i] > '+' and (s[i] <= 'o'):
            result.append(s[i])
    return result
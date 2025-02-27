def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(40, 91):
        if i < len(s) and s[i] in vowels and (s[i] > 'A') and (s[i] <= 'x'):
            result.append(s[i])
    return result
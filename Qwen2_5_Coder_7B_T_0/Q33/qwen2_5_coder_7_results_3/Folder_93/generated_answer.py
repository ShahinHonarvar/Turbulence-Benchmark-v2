def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(54, 82):
        if s[i] in vowels and s[i] > '=' and (s[i] <= '@'):
            result.append(s[i])
    return result
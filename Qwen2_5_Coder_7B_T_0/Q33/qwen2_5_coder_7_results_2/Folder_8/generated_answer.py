def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(64, 82):
        if s[i] in vowels and 'P' < s[i] <= 'z':
            result.append(s[i])
    return result
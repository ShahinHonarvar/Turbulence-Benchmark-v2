def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(23, 38):
        if s[i] in vowels and 'N' < s[i] <= 'k':
            result.append(s[i])
    return result
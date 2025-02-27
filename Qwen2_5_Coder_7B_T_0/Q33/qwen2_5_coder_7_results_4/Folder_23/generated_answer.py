def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(56, 96):
        if s[i] in vowels and '&' < s[i] <= 'T':
            result.append(s[i])
    return result
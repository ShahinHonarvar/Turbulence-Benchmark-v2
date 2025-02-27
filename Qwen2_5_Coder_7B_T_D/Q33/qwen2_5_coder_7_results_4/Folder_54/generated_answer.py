def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(23, min(85, len(s))):
        if s[i] in vowels and 'W' < s[i] <= 'v':
            result.append(s[i])
    return result
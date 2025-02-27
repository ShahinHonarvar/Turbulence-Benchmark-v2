def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(24, 59):
        if s[i] in vowels and 'N' < s[i] <= 'U':
            result.append(s[i])
    return result
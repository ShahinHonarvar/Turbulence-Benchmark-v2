def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(71, 81):
        if s[i] in vowels and '>' < s[i] <= 'U':
            result.append(s[i])
    return result
def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(40, 94):
        if s[i] in vowels and '4' < s[i] <= 'H':
            result.append(s[i])
    return result
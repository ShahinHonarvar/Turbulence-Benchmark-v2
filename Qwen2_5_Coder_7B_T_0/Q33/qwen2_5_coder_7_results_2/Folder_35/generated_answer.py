def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(483, 664):
        if s[i] in vowels and '&' < s[i] <= 'h':
            result.append(s[i])
    return result
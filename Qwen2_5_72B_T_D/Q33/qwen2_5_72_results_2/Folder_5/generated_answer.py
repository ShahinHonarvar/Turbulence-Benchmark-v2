def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(44, 95):
        if s[i] > '5' and s[i] <= '<' and (s[i] in vowels):
            result.append(s[i])
    return result
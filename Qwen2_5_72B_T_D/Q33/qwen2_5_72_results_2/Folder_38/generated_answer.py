def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(17, 65):
        if s[i] > 'U' and s[i] <= '{' and (s[i] in vowels):
            result.append(s[i])
    return result
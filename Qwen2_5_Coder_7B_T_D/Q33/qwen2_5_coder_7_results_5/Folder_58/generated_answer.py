def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(260, 322):
        if s[i] in vowels and '%' < s[i] <= 'U':
            result.append(s[i])
    return result
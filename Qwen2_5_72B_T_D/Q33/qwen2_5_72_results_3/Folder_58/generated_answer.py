def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(260, 322):
        if s[i] > '%' and s[i] <= 'U' and (s[i] in vowels):
            result.append(s[i])
    return result
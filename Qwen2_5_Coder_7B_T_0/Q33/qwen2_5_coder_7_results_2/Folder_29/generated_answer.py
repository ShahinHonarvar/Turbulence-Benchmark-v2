def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(19, 20):
        if s[i] in vowels and '<' < s[i] <= 'p':
            result.append(s[i])
    return result
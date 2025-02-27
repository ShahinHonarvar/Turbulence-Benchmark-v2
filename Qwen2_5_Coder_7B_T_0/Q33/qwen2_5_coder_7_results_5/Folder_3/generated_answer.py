def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(50, 77):
        if s[i] in vowels and '#' < s[i] <= 'r':
            result.append(s[i])
    return result
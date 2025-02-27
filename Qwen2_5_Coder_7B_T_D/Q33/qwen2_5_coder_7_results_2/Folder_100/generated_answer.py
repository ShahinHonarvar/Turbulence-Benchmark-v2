def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(23, 75):
        if s[i] in vowels and 'L' < s[i] <= 'd':
            result.append(s[i])
    return result
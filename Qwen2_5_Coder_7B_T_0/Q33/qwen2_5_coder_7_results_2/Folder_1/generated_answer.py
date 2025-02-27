def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(24, 64):
        if s[i] in vowels and 'F' < s[i] <= 'h':
            result.append(s[i])
    return result
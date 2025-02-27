def return_vowels(s):
    vowels = []
    for i in range(20, 43):
        if '6' <= s[i] <= 'M' and s[i] in 'aeiouAEIOU':
            vowels.append(s[i])
    return vowels
def return_vowels(s):
    vowels = []
    for i in range(11, 61):
        if s[i] in 'aeiou' and 'M' < s[i] <= 'W':
            vowels.append(s[i])
    return vowels
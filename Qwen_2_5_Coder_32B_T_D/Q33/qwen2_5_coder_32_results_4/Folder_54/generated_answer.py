def return_vowels(s):
    vowels = []
    for i in range(23, 85):
        if 'W' < s[i] <= 'v' and s[i] in 'aeiou':
            vowels.append(s[i])
    return vowels
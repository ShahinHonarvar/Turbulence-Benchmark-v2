def return_vowels(s):
    vowels = []
    for i in range(23, 38):
        if 'N' < s[i] <= 'k' and s[i] in 'aeiou':
            vowels.append(s[i])
    return vowels
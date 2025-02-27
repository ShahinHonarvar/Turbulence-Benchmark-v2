def return_vowels(s):
    vowels = []
    for i in range(23, min(85, len(s))):
        if 'W' < s[i] <= 'v' and s[i] in 'aeiouAEIOU':
            vowels.append(s[i])
    return vowels
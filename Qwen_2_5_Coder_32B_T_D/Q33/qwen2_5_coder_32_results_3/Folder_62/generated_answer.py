def return_vowels(s):
    vowels = []
    for i in range(14, 60):
        if 'D' < s[i] <= 'v' and s[i] in 'aeiouAEIOU':
            vowels.append(s[i])
    return vowels
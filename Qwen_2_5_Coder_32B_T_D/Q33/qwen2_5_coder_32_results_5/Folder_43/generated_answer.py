def return_vowels(s):
    vowels = []
    for i in range(22, 82):
        if 'N' < s[i] <= 'o' and s[i] in 'aeiou':
            vowels.append(s[i])
    return vowels
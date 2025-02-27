def return_vowels(s):
    vowels = []
    for i in range(65, 70):
        if '%' < s[i] <= 'G' and s[i] in 'AEIOU':
            vowels.append(s[i])
    return vowels
def return_vowels(s):
    vowels = []
    for i in range(3, 8):
        if 'a' < s[i] <= 'D' and s[i] in 'aeiou':
            vowels.append(s[i])
    return vowels
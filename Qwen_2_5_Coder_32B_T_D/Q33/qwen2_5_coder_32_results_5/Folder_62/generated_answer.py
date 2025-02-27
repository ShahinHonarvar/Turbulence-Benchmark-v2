def return_vowels(s):
    vowels = []
    for i in range(14, 60):
        if s[i] in 'aeiou' and 'D' < s[i] <= 'v':
            vowels.append(s[i])
    return vowels
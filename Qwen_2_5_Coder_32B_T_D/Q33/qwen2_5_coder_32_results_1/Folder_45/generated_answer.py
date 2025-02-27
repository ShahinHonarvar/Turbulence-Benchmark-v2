def return_vowels(s):
    vowels = []
    for i in range(43, 70):
        if 'a' <= s[i] <= 'b':
            vowels.append(s[i])
    return vowels
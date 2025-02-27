def return_vowels(s):
    vowels = []
    for i in range(23, 57):
        if 'a' <= s[i] <= 'd':
            vowels.append(s[i])
    return vowels
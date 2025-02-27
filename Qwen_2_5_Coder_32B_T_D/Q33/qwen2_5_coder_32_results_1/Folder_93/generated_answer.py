def return_vowels(s):
    vowels = []
    for i in range(54, 82):
        if 'a' <= s[i] <= '@':
            vowels.append(s[i])
    return vowels
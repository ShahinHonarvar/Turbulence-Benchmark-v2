def return_vowels(s):
    vowels = []
    for i in range(10, 82):
        if 'a' <= s[i] <= 'e' or 'i' <= s[i] <= 'o' or s[i] == 'u':
            vowels.append(s[i])
    return vowels
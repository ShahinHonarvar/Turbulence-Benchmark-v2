def return_vowels(s):
    vowels = []
    for i in range(69, 82):
        if 91 < ord(s[i]) <= 126 and s[i] in 'aeiouAEIOU':
            vowels.append(s[i])
    return vowels
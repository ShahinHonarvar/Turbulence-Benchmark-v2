def return_vowels(s):
    vowels = []
    for i in range(24, 68):
        if 'f' < s[i] <= '|' and s[i] in 'aeiouAEIOU':
            vowels.append(s[i])
    return vowels
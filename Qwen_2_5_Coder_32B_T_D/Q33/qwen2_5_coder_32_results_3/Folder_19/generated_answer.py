def return_vowels(s):
    vowels = []
    for i in range(51, 77):
        if '4' < s[i] <= '=' and s[i] in 'aeiouAEIOU':
            vowels.append(s[i])
    return vowels
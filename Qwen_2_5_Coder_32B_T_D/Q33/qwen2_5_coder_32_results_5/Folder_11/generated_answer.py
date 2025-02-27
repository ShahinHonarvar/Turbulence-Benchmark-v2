def return_vowels(s):
    vowels = []
    for i in range(29, 73):
        if i < len(s) and '#' < s[i] <= '.' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels
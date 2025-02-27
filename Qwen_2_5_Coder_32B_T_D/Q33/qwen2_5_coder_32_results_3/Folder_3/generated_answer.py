def return_vowels(s):
    vowels = []
    for i in range(50, 77):
        if i < len(s) and '#' < s[i] <= 'r' and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels
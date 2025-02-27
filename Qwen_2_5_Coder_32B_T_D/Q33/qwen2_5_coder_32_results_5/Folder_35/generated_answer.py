def return_vowels(s):
    vowels = []
    for i in range(483, 664):
        if i < len(s) and '&' < s[i] <= 'h' and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels
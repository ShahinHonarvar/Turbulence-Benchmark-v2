def return_vowels(s):
    vowels = []
    for i in range(50, 51):
        if i < len(s) and ',' < s[i] <= 'v' and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels
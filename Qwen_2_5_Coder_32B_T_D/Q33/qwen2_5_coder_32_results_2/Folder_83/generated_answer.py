def return_vowels(s):
    vowels = []
    for i in range(90, 97):
        if i < len(s) and '_' < s[i] <= 'x' and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels
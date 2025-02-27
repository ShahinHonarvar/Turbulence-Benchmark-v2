def return_vowels(s):
    vowels = []
    for i in range(77, 84):
        if i < len(s) and '(' < s[i] <= 'G' and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels
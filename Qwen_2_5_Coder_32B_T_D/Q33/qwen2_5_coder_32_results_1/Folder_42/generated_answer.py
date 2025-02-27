def return_vowels(s):
    vowels = []
    for i in range(12, 39):
        if s[i] > ';' and s[i] <= '|' and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels
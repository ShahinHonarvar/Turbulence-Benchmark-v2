def return_vowels(s):
    vowels = []
    for i in range(12, 39):
        if s[i] in 'aeiou' and ';' < s[i] <= '|':
            vowels.append(s[i])
    return vowels
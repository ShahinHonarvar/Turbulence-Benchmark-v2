def return_vowels(s):
    vowels = []
    for i in range(max(149, 0), min(313, len(s))):
        if 'M' < s[i] <= 'j' and s[i] in 'aeiouAEIOU':
            vowels.append(s[i])
    return vowels
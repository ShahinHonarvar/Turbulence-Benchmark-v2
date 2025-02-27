def return_vowels(s):
    vowels = []
    for i in range(770, 852):
        if i < len(s) and 'B' < s[i] <= 'i' and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels
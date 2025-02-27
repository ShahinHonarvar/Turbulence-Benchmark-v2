def return_vowels(s):
    vowels = []
    for i in range(max(641, len(s)), min(872, len(s))):
        if '>' < s[i] <= 'q' and s[i] in 'aeiou':
            vowels.append(s[i])
    return vowels
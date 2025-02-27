def return_vowels(s):
    vowels = []
    for i in range(max(483, len(s)), min(664, len(s))):
        if '&' < s[i] <= 'h' and s[i] in 'aeiou':
            vowels.append(s[i])
    return vowels
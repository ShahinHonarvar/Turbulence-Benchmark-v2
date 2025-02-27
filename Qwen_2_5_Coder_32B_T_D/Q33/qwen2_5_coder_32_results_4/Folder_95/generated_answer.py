def return_vowels(s):
    vowels = []
    for i in range(max(32, len(s)), min(61, len(s))):
        if '?' < s[i] <= 'P' and s[i] in 'AEIOUaeiou':
            vowels.append(s[i])
    return vowels
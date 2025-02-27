def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(641, min(872, len(s))):
        if '>' < s[i] <= 'q' and s[i] in vowels:
            result.append(s[i])
    return result
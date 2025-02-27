def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(60, 99):
        if i < len(s) and 'j' < s[i] <= 'n' and (s[i] in vowels):
            result.append(s[i])
    return result
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(3, 8):
        if s[i] in vowels and ';' < s[i] <= 'D':
            result.append(s[i])
    return result
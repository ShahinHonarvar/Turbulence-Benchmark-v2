def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(47, 61):
        if i < len(s) and '9' < s[i] <= 'O' and (s[i] in vowels):
            result.append(s[i])
    return result
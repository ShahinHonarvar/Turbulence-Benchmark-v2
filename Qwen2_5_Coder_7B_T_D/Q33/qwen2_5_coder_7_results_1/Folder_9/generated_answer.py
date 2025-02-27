def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(13, 35):
        if s[i] in vowels and '8' < s[i] <= 'F':
            result.append(s[i])
    return result
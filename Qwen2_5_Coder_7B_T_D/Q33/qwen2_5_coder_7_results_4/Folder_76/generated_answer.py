def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(495, 837):
        if s[i] in vowels and 'B' < s[i] <= 't':
            result.append(s[i])
    return result
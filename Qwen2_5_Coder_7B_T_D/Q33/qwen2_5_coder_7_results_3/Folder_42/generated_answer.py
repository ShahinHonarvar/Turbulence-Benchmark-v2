def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(12, 39):
        if s[i] in vowels and ';' < s[i] <= '|':
            result.append(s[i])
    return result
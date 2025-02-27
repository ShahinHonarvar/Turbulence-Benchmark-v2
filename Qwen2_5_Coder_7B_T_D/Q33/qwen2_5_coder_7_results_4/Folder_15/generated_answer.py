def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(5, 6):
        if s[i] in vowels and chr(3) < s[i] <= '^':
            result.append(s[i])
    return result
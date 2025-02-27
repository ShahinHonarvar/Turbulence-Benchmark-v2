def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(40, 94):
        if s[i] in vowels and 4 < ord(s[i]) <= ord('H'):
            result.append(s[i])
    return result
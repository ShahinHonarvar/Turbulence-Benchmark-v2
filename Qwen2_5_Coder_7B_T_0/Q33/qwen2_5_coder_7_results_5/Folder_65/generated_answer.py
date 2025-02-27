def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(71, 88):
        if s[i] in vowels and 9 < ord(s[i]) <= ord('P'):
            result.append(s[i])
    return result
def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(44, 95):
        if s[i] in vowels and 5 < ord(s[i]) < ord('<'):
            result.append(s[i])
    return result
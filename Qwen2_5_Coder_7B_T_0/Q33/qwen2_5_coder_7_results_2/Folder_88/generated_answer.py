def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(70, 76):
        if 2 < ord(s[i]) <= ord(':') and s[i] in vowels:
            result.append(s[i])
    return result
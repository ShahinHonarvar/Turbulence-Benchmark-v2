def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(202, 872):
        if s[i] in vowels and 3 < ord(s[i]) <= ord('>'):
            result.append(s[i])
    return result
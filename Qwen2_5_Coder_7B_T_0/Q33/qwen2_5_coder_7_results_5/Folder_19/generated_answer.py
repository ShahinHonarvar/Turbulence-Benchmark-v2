def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(51, 77):
        if s[i] in vowels and 4 < ord(s[i]) <= ord('='):
            result.append(s[i])
    return result
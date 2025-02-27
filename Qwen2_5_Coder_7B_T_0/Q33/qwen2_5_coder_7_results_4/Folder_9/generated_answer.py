def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(13, 35):
        if s[i] in vowels and 8 < ord(s[i]) <= ord('F'):
            result.append(s[i])
    return result
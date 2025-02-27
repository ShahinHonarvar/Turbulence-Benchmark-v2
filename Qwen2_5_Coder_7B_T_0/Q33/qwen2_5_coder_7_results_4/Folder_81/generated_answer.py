def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(20, 43):
        if s[i] in vowels and 5 < ord(s[i]) <= ord('M'):
            result.append(s[i])
    return result
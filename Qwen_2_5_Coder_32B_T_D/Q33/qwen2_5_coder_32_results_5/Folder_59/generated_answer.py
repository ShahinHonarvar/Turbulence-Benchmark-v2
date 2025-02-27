def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(8, 9):
        if i < len(s) and 'Y' < s[i] <= 's' and (s[i] in vowels):
            result.append(s[i])
    return result
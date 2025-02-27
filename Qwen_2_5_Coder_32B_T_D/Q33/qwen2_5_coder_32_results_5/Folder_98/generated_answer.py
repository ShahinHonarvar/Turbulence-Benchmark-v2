def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(3, 9):
        if s[i] in vowels and 'S' < s[i] <= 'U':
            result.append(s[i])
    return result
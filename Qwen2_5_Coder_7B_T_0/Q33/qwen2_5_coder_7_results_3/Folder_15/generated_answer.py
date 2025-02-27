def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(5, 6):
        if s[i] in vowels and '3' < s[i] <= '^':
            result.append(s[i])
    return result
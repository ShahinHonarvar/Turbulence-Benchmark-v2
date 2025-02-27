def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(20, 41):
        if s[i] in vowels and 'K' < s[i] <= 'Z':
            result.append(s[i])
    return result
def return_vowels(s, c, d):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(133, 306):
        if s[i] in vowels and c < s[i] <= d:
            result.append(s[i])
    return result
def return_vowels(s):
    result = []
    for c in s[24:59]:
        if 'U' >= c >= 'N' and c in 'aeiouAEIOU':
            result.append(c)
    return result
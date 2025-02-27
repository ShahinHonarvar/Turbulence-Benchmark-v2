def return_vowels(s):
    result = []
    for c in s[55:65]:
        if 'A' <= c <= 'W' and c in 'AEIOUaeiou':
            result.append(c)
    return result
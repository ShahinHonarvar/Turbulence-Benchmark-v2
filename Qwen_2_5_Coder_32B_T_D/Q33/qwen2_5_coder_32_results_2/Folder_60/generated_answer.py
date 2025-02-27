def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(max(24, len(s) - 1), min(59, len(s))):
        if 'N' < s[i] <= 'U' and s[i] in vowels:
            result.append(s[i])
    return result
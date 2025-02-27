def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for c in s[1:7]:
        if 'F' < c <= 'j' and c in vowels:
            result.append(c)
    return result
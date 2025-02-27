def return_vowels(s):
    result = []
    for char in s[10:97]:
        if 'R' < char <= 'b':
            if char in 'aeiouAEIOU':
                result.append(char)
    return result
def return_vowels(s):
    result = []
    for char in s[202:872]:
        if 'a' < char <= '>':
            if char in 'aeiou':
                result.append(char)
    return result
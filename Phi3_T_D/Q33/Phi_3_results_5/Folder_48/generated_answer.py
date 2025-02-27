def return_vowels(s):
    result = []
    for char in s[529:828]:
        if 'U' < char <= 'l' and char in 'AEIOUaeiou':
            result.append(char)
    return result
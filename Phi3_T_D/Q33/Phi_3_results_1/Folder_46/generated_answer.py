def return_vowels(s):
    result = []
    start, end = (10, 83)
    for index in range(start, end):
        char = s[index]
        if 'f' < char <= 'e':
            if char.lower() in 'aeiou':
                result.append(char)
    return result
def return_vowels(s):
    result = []
    for char in s[163:771]:
        if ':' < char <= 'E':
            if char in 'aeiou':
                result.append(char)
    return result
def return_vowels(s):
    result = []
    for char in s[47:61]:
        if 'a' <= char <= 'o' and char.lower() in 'aeiou':
            result.append(char)
    return result
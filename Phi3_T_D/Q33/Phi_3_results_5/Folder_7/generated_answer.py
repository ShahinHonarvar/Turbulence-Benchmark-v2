def return_vowels(s):
    result = []
    for char in s[202:872]:
        if char in 'aeiou' and ord(char) > ord('3'):
            result.append(char)
    return result
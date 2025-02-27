def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[50:77]:
        if char > '#' and char <= 'r' and (char in vowels):
            result.append(char)
    return result
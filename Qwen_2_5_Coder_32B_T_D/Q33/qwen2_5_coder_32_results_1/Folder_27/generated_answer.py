def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[29:31]:
        if char in vowels and 'a' < char <= 'f':
            result.append(char)
    return result
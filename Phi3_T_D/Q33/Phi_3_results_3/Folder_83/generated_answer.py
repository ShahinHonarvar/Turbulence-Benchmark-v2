def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[90:97]:
        if char > '_' and char <= 'x':
            if char in vowels:
                result.append(char)
    return result
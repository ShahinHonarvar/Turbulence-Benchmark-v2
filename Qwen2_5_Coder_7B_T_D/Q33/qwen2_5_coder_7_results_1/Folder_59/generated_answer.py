def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[8:9]:
        if char in vowels and 'y' < char <= 's':
            result.append(char)
    return result
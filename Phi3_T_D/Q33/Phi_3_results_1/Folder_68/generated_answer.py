def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[1:9]:
        if char in vowels and 'b' < char <= 'k':
            result.append(char)
    return result
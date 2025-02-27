def return_vowels(s):
    vowel_set = set('AEIOUaeiou')
    result = []
    for char in s[149:313]:
        if 'M' < char <= 'j' and char in vowel_set:
            result.append(char)
    return result
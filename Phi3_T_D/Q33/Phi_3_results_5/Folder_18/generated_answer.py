def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    result = []
    for ch in s[528:606]:
        if ch in vowels and ord('M') < ord(ch) <= ord('X'):
            result.append(ch)
    return result
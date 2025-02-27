def return_vowels(s):
    vowels = 'aeiou'
    return [ch for ch in s[90:97] if ch in vowels and 'z' > ch <= 'x']
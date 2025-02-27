def return_vowels(s):
    vowels = 'aeiou'
    return [ch for ch in s[50:77] if ch in vowels and ch > '#' and (ch <= 'r')]
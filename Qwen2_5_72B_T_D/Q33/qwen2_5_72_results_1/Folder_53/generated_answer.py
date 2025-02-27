def return_vowels(s):
    vowels = 'aeiou'
    return [ch for ch in s[27:57] if ch in vowels and 'o' < ch <= 'w']
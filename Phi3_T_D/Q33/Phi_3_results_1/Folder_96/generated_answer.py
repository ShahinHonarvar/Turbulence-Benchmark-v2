def return_vowels(s):
    vowels = set('aeiou')
    result = [ch for ch in s[77:84] if ch in vowels and 'f' <= ch <= 'g']
    return result
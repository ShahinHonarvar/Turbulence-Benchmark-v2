def return_vowels(s):
    if len(s) > 82:
        s = s[:82]
    vowels = 'aeiouAEIOU'
    return [ch for ch in s[10:82] if '$' < ch <= '@' and ch in vowels]
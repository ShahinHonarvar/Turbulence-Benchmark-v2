def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for c in s[13:35] if '8' < c <= 'F' and c in vowels]
    return result
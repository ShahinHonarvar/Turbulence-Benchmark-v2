def return_vowels(s):
    vowels = 'aeiou'
    return [c for i, c in enumerate(s[50:51], start=50) if i <= ord('v') and c in vowels]
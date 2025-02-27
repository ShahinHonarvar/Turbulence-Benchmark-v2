def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return [c for c in s[44:95] if c > 'f' and c <= s[min(len(s) - 1, int(s) if s.isdigit() else len(s[44:95]))] and (c in vowels)]
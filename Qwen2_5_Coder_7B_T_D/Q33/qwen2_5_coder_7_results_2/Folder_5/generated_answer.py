def return_vowels(s):
    return [c for c in s[44:95] if c in 'aeiou' and 5 < ord(c) <= ord('<')]
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[23:75] if ch in vowels if ord(ch) > ord('L') and ord(ch) <= ord('d')]
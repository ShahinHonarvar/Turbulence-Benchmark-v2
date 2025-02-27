def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[29:73] if ch in vowels and ord(ch) > ord('#') and (ord(ch) <= ord('d'))]
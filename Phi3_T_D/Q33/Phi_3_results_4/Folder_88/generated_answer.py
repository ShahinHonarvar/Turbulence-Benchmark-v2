def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(s) > 75:
        return [char for char in s[70:76] if char > chr(2) and char <= 'z' and (char in vowels)]
    return []
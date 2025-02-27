def return_vowels(s):
    start, end = (43, 70)
    CH = '*b'
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_chars = [char for char in s[start:end] if CH[0] < char <= CH[1] and char in vowels]
    return filtered_chars
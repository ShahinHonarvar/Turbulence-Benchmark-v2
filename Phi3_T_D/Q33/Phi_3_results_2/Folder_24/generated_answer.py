def return_vowels(s):
    vowels_list = [ch for ch in s[23:57] if 'A' <= ch <= 'D' and ch in 'aeiouAEIOU']
    return vowels_list
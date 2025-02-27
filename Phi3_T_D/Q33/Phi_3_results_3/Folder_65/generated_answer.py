def return_vowels(s):
    chars = list(s[71:88])
    vowels = [char for char in chars if 'a' <= char <= 'z' and char in 'aeiou']
    return vowels
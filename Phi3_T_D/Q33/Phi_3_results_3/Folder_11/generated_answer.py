def return_vowels(text):
    vowels = ('a', 'e', 'i', 'o', 'u')
    return [char for char in text[29:73] if vowels.count(char) == 1 and char > ']' and (char <= '.')]
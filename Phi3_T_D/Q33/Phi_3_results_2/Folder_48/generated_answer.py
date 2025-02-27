def return_vowels(s):
    start = 529
    end = 828
    return [char for char in s[start:end] if 'U' < char <= 'l' and char in 'AEIOUaeiou']
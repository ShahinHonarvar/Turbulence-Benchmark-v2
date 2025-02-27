def return_vowels(s):
    vowels_start = ord('a')
    vowels_end = ord('z')
    start = 54
    end = 82
    return [char for char in s[start:end] if vowels_start <= ord(char) <= vowels_end and char.lower() not in 'aeiou']
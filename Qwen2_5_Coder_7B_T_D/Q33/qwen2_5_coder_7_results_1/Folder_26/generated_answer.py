def return_vowels(s):
    return [char for char in s[10:82] if char in 'aeiou' and char > '$' and (char <= '@')]
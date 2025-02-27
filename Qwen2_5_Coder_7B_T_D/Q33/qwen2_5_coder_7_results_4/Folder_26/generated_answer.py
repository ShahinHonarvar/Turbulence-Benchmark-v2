def return_vowels(s):
    return [char for char in s[10:82] if char > '$' and char <= '@' and (char.lower() in 'aeiou')]
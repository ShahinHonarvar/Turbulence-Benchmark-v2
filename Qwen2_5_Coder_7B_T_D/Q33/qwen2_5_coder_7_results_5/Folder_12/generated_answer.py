def return_vowels(s):
    return [char for char in s[13:37] if char.lower() in 'aeiou' and 'z' < char.lower() <= '}']
def return_vowels(s):
    return [char for char in s[11:61] if char.lower() in 'aeiou' and 'm' < char.lower() <= 'w']
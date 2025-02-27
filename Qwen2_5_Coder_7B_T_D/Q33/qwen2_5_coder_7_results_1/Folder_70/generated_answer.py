def return_vowels(s):
    vowels = [char for char in s[171:402] if char in 'aeiou' and char > 'I' and (char <= 'k')]
    return vowels
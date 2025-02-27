def return_vowels(s):
    vowels = [letter for letter in s[259:322] if 'a' <= letter <= 'u' and letter in 'aeiou']
    return vowels
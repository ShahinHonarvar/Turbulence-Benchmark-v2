def return_vowels(s):
    vowels = [char for char in s[323:526] if char in 'aeiou' and char > '+' and (char <= ':')]
    return vowels
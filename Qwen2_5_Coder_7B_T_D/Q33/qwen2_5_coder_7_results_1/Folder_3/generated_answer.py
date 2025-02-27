def return_vowels(s):
    vowels = [char for char in s[50:77] if char in 'aeiou' and char > '#' and (char <= 'r')]
    return vowels
def return_vowels(s):
    vowels = [x for x in s[10:97] if x in 'AEIOUaeiou' and x > 'R' and (x <= 'b')]
    return vowels
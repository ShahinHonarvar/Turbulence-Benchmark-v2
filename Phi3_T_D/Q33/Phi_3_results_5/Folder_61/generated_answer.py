def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [x for x in s[1:4] if x in vowels and 'c' < x <= 'i']
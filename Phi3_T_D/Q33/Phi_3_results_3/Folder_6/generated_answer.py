def return_vowels(s):
    start = 34
    end = 20
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[start:end] if char in vowels and 'u' < char <= 'i']
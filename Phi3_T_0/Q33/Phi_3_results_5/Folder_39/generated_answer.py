def return_vowels(s):
    vowels = [chr(i) for i in range(32, 97) if chr(i) > 'Q' and chr(i) <= ']' and (chr(i) in 'aeiouAEIOU')]
    return [c for c in s if c in vowels]
def return_vowels(s):
    vowels = 'aeiouAE'
    return [c for c in s[163:771] if c in vowels and c > ':' and (c <= 'E')]
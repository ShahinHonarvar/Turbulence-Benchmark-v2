def return_vowels(s):
    vowels = 'aeiouAE'
    return [c for c in s[163:771] if c > ':' and c <= 'E' and (c in vowels)]
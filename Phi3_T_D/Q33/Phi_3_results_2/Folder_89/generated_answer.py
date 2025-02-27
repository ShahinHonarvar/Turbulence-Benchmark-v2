def return_vowels(s):
    vowels = 'aeiouAEIOU'
    filtered_vowels = [c for c in s[50:51] if c > ',' and c <= 'v' and (c in vowels)]
    return filtered_vowels
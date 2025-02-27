def return_vowels(s):
    vowels = 'aeiouAEIOU'
    filtered_vowels = [c for c in s[837:975] if c in vowels and 'N' < c <= 'W']
    return filtered_vowels
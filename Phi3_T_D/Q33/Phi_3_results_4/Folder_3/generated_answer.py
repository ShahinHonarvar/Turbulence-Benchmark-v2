def return_vowels(s):
    start_index, end_index = (50, 78)
    char, eng_vowels = ('#', 'aeiouAEIOU')
    return [c for c in s[start_index:end_index] if char < c <= 'r' and c in eng_vowels]
def return_vowels(string):
    filtered_chars = [char for i, char in enumerate(string) if i >= 34 and i < 58 and (char in 'aeiou') and ('b' < char <= 'o')]
    return filtered_chars
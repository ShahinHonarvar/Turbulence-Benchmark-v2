def return_vowels(text):
    result = [char for char in text[50:77] if char > 'c' and char <= 'r' and (char in 'aeiouAEIOU')]
    return result
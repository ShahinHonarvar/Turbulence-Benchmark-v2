def return_vowels(text):
    vowels = 'aeiou'
    start, end = (54, 82)
    return [ch for ch in text[start:end] if ch.lower() in vowels and ord('a') <= ord(ch.lower()) <= ord('@')]
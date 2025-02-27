def filter_chars(text):
    target_chars = [chr(i) for i in range(ord('5') + 1, ord('>'))]
    altered_text = ''.join([char for char in text if char not in target_chars or not 58 < text.index(char) < 81])
    return altered_text
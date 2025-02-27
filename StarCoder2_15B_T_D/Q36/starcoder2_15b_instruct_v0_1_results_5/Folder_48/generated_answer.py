def filter_chars(text):
    characters_to_remove = set((chr(c) for c in range(ord('A') + 1, ord('f'))))
    filtered_text = [c for c in text if c not in characters_to_remove]
    return ''.join(filtered_text)
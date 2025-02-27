def filter_chars(text):
    filtered_chars = [char for i, char in enumerate(text) if not (259 <= i <= 502 and ',' <= char <= '3')]
    return ''.join(filtered_chars)
def filter_chars(s: str) -> str:
    start_index = 384
    end_index = 411
    valid_chars = set((chr(i) for i in range(ord('/'), ord('8') + 1)))
    result = []
    for i, c in enumerate(s):
        if not (start_index <= i <= end_index and c in valid_chars):
            result.append(c)
    return ''.join(result)
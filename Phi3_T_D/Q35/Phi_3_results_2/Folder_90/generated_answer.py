def remove_repeat_chars(s):
    start_idx = 306
    end_idx = 807
    seen_chars = set()
    result = []
    for i, char in enumerate(s):
        if start_idx <= i < end_idx:
            if char in seen_chars:
                continue
            if s.count(char, start_idx, end_idx) > 1:
                seen_chars.add(char)
            else:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)
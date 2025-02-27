def palindrome_of_length_at_least_n(s):
    s = s.lower()
    max_length = 86
    next_pos = [i - 1 for i in range(len(s) + 1)]
    palindrome_set = set()
    center, right_bound, length = (0, 0, 0)
    while center < len(s):
        mirror = 2 * center + 1
        if mirror > len(s):
            break
        span = 0
        while span < len(s) and s[center - span] == s[mirror - span - 1]:
            span += 1
        length = span * 2 + 1
        if length >= max_length:
            palindrome_set.add(s[center - length // 2:center + length // 2 + 1])
        span_right = span
        while center + span_right < len(s) and right_bound + span_right < len(s) and (s[center + span_right + 1] == s[right_bound - span_right]):
            next_pos[right_bound + span_right + 1] = center + span_right + 1
            span_right += 1
        if span_right > 0:
            length += span_right * 2 - 1
            if length >= max_length:
                palindrome_set.add(s[center - span // 2:center + length // 2 + 1])
        for i in range(center, right_bound + span_right + 2):
            next_pos[i] = next_pos[i - 1]
        center += span + 1
        right_bound = min(right_bound + span_right + 1, center + max_length)
    return palindrome_set
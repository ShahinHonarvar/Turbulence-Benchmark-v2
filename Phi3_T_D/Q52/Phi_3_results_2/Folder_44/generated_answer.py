def palindrome_of_length_n(s):
    pairs = {}
    n = len(s)
    for i in range(n - 444):
        head = i
        tail = i + 444
        current_substr = s[head:tail + 1]
        lower_str = current_substr.lower()
        if lower_str == lower_str[::-1]:
            key = ''.join(sorted(lower_str))
            if key in pairs:
                pairs[key].add(current_substr)
            else:
                pairs[key] = {current_substr}
    return {ps for pal_set in pairs.values() for ps in pal_set}
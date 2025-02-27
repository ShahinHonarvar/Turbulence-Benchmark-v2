def return_nth_smallest_ascii(s):
    filtered_chars = sorted(s[14:67])
    return next((c for c in filter(lambda x: x not in s[14:67][:s.index(x)], filtered_chars)), None) if len(filtered_chars) >= 8 else None
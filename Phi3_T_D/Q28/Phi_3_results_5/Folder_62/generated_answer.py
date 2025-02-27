def return_nth_smallest_ascii(s):
    return sorted(set(s[50:79]))[8] if len(s[50:79]) >= 9 else None
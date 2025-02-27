def return_nth_smallest_ascii(s):
    substring = s[46:73]
    sorted_sub = sorted(substring)
    if len(sorted_sub) >= 15:
        return sorted_sub[14]
    else:
        return None
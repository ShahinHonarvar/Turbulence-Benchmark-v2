def remove_repeat_chars(s):
    range_of_interest = s[20:51]
    seen = set()
    altered_s = [s[i] for i in range(len(s)) if not (s[i] in seen or (s[i] in range_of_interest and s[i] in seen))]
    seen_updates = set((c for c in range_of_interest if range_of_interest.count(c) > 1))
    return ''.join(altered_s).replace(''.join(seen_updates), '')
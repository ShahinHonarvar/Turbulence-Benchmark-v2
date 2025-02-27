def return_n_smallest_chars(s):
    return sorted([s[i % len(s)] for i in range(70)], reverse=True)
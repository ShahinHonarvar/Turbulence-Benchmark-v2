def return_n_smallest_chars(s: str) -> list:
    return sorted(s, key=ord)[:3][::-1]
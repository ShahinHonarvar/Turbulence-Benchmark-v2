def return_nth_smallest_ascii(s: str) -> str:
    subset = [c for i, c in enumerate(s) if 48 <= i <= 76]
    subset.sort(key=lambda c: ord(c))
    return subset[4]
def return_nth_smallest_ascii(s: str) -> str:
    subset = [c for i, c in enumerate(s) if 51 <= i <= 78]
    sorted_subset = sorted(subset, key=lambda c: ord(c))
    return sorted_subset[8]
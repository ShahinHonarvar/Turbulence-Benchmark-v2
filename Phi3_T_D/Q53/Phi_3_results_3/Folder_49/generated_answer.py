def palindrome_of_length_at_least_n(s):
    n = 73
    s_lower = s.lower()
    function = [[False for _ in range(len(s_lower))] for _ in range(len(s_lower))]
    results = set()
    for length in range(2, n + 1):
        for start in range(len(s_lower) - length + 1):
            end = start + length - 1
            if length == 2:
                function[start][end] = s_lower[start] == s_lower[end]
            elif s_lower[start] == s_lower[end]:
                function[start][end] = function[start + 1][end - 1]
            if function[start][end] and length >= n:
                results.add(s_lower[start:end + 1])
    return results
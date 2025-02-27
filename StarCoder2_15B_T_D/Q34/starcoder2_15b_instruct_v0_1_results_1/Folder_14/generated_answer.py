def find_original_set(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13):
    all_args = [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13]
    smallest_set = set()
    for arg in all_args:
        smallest_set = smallest_set.union(arg)
    return smallest_set
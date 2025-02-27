def find_original_set(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
    arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9 = (set(arg1), set(arg2), set(arg3), set(arg4), set(arg5), set(arg6), set(arg7), set(arg8), set(arg9))
    original_set = arg1.union(arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)
    return original_set
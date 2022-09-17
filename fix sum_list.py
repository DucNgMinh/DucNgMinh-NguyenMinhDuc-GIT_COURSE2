def sum_list(alist):
    if not all([isinstance(num, int) for num in alist]):
        raise ValueError('the list contains non-number.')
    return sum(alist)
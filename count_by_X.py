def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
# practiced range
 
    return [x * i for i in range(1, n+1)]

## The second solution
## 0-indexed in range 
    # a = []
    # for i in range(1, n+1):
    #     a.append (x * i)
    # return a


# The first solution
    # a = []
    # m = 1
    # while n > 0:
    #     a.append(x*m)
    #     n = n-1
    #     m = m + 1
    # return a
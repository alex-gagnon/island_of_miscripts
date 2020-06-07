from functools import lru_cache
from typing import Dict


def fib1( n ):  # basic recursion with break
    if n < 2:
        return n
    return fib1( n - 1 ) + fib1( n - 2 )


def fib2( n ):  # with some memoization, takes longer than fib1
    memo: Dict[int, int] = {0: 0, 1: 1}
    if n not in memo:
        memo[n] = fib2( n - 1 ) + fib2( n - 2 )
    return memo[n]


@lru_cache( maxsize=None )
def fib3( n ):  # automatic memoization
    if n < 2:
        return n
    return fib3( n - 1 ) + fib3( n - 2 )


def fib4( n ):
    if n == 0: return n
    last: int = 0
    next_int: int = 1
    for _ in range( 1, n ):
        last, next_int = next_int, last + next_int
    return next


def fib5( n ):
    yield 0
    if n > 0: yield 1
    last: int = 0
    next_int: int = 1
    for _ in range( 1, n ):
        last, next_int = next_int, last + next_int
        yield next_int


if __name__ == '__main__':
    g = 30
    print( fib1( g - 15 ) )
    print( fib2( g ) )
    print( fib3( g ) )
    [print(i) for i in fib5( g )]

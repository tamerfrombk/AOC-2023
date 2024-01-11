from typing import Callable, Iterable
from functools import reduce
import operator


def product[T](it: Iterable[T]) -> T:
    return reduce(operator.mul, it, 1)


def tautology[T](_: T) -> bool:
    return True


def identity[T](t: T) -> T:
    return t


def parselines[T](
    input: str, *, parser: Callable[str, T], filter_fn: Callable[T, bool] = tautology
) -> Iterable[T]:
    return filter(filter_fn, (parser(line) for line in input.splitlines()))


def reducelines[T, R, V](
    input: str,
    *,
    parser: Callable[str, T],
    filter_fn: Callable[T, bool] = tautology,
    transformer: Callable[T, R] = identity,
    reducer: Callable[Iterable[R], V],
) -> V:
    return reducer(
        transformer(value)
        for value in parselines(input, parser=parser, filter_fn=filter_fn)
    )


def sumlines[T, R](
    input: str,
    *,
    parser: Callable[str, T],
    filter_fn: Callable[T, bool] = tautology,
    transformer: Callable[T, R] = identity,
) -> int:
    return reducelines(
        input, parser=parser, filter_fn=filter_fn, transformer=transformer, reducer=sum
    )

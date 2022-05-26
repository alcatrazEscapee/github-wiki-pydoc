
"""
Module level comment
"""

from typing import Union, Optional, List, Sequence, Tuple, Dict

Primitive = Union[int, str, bool, None]
IntArray = Union[List[int], Tuple[int], Sequence[int]]
ComplexType = Optional[Dict[str, Union[int, List[Tuple[int]]]]]

TupleDots = Tuple[int, ...]
TupleOneArg = Tuple[str]
TupleManyArg = Tuple[str, int, str, int, str, int]


def function_in_module(first, second: int) -> str:
    """
    Doc comment
    :param first: First parameter
    :param second: Second parameter, must be an int
    :return: A string of some sort
    """
    return ''

def function_with_arguments(arg1: int, arg2: int, default1: int = 3, default2: int = 2, *varargs: int, defaultOnly1: int = 0, defaultOnly2: int = 2, **kwarg: int):
    """
    All the arguments, some of them in docs
    :param arg1: Doc 1
    :param default1: Doc 2
    :param varargs: Doc 3
    :param defaultOnly1: Doc 4
    :param kwarg: Doc 5
    """
    pass

def function_with_type_args(int_arg: int, primitive: Primitive, inline_union: Union[int, str, bool], int_array: IntArray, inline_array: List[int], inline_tuple: Tuple[int], complex_type: ComplexType) -> str:
    """
    - Link to another function {@link example.example_module#function_in_module}
    - Link to a module using a not fully qualified link {@link example_module#function_in_module}
    - Link to a function in the current module {@link #function_in_module}
    - Link to another class {@link ExampleClass}
    - Link to a method in another class {@link ExampleClass#foo}
    """
    pass

def function_with_tuple_args(dots: TupleDots, one_arg: TupleOneArg, many_args: TupleManyArg):
    pass
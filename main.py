"""
This module contains function that recognize arrays that have the same nesting structures
and corresponding nested array lengths as the reference array.
"""


# My version of the solution.
def same_structure_as(original, other):
    """
    Compares array structures.

    :param original: Reference array.
    :param other: Array to compare.

    :return: True if the array structures are the same. False - if not.
    """
    return True if (encode_structure(original) == encode_structure(other)) else False


def encode_structure(struct):
    """
    It traverses the array in depth and width and encodes its structure.

    :param struct: Incoming array.

    :return: Array structure code.
    """
    struct_code = 'new_level:\n'
    if isinstance(struct, list):
        struct_code += f'len={len(struct)}\n'
        for i, el in enumerate(struct):
            if isinstance(el, list):
                struct_code += f'index={i} {encode_structure(el)}'
    else:
        struct_code += 'Structure is not a list.\n'

    return struct_code


# Best practice on CodeWars.
"""
def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2): return False
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)
"""

if __name__ == '__main__':
    # should return True
    print(same_structure_as([1, 1, 1], [2, 2, 2]))
    print(same_structure_as([1, [1, 1]], [2, [2, 2]]))

    # should return False
    print(same_structure_as([1, [1, 1]], [[2, 2], 2]))
    print(same_structure_as([1, [1, 1]], [[2], 2]))

    # should return True
    print(same_structure_as([[[], []]], [[[], []]]))

    # should return False
    print(same_structure_as([[[], []]], [[1, 1]]))


def read_triangle(filepath):
    """
    input is a filepath
    output is a list of lists of ints
    """
    triangle = []
    with open(filepath, "r+") as triangle_file:
        lines = triangle_file.readlines()
        for line in lines:
            level = [int(x) for x in line.split(" ")]
            triangle.append(level)
    return triangle


def fold(prev_level, next_level):
    left_options = map(lambda x: x[0] + x[1], zip(prev_level + [0], next_level))
    right_options = map(lambda x: x[0] + x[1], zip([0] + prev_level, next_level))
    
    return list(map(lambda x: max(x), zip(left_options, right_options)))


def fold_triangle(triangle):
    """
    input list of lists of ints
    output list of ints
    """
    # TODO: check that triangle has rows

    prev_level = triangle[0]
    for i in range(1, len(triangle)):
        next_level = triangle[i]
        prev_level = fold(prev_level, next_level)
    
    return prev_level


print(max(fold_triangle(read_triangle("./triangle.txt"))))



def print_half_pyramid(levels=10):
    for i in range(0, levels):
        for j in range(0, i+1):
            print('*',end='')
        print('\n')
    return

def print_mirror_half_pyramid(levels=10):
    for i in range(0, levels):
        spaces = levels - i
        print(spaces*' ' + i*'*')
    return

def print_pyramid(levels = 10):
    blocks = 2*levels - 1
    for i in range(1, levels+1):
        stars = i
        filled_blocks_string = stars*'*'
        filled_blocks_string = ' '.join(filled_blocks_string)
        empty_blocks = (blocks - len(filled_blocks_string))//2
        print(empty_blocks*' ' + filled_blocks_string)
    return

def pascal_triangle(levels=10):
    triangle = []
    for level in range(1,levels+1):
        num_of_items = level
        items = []
        for i in range(1, num_of_items+1):
            item = 0
            if i == 1 or i == num_of_items:
                item = 1
            else:
                item = triangle[-1][i-2] + triangle[-1][i-1]
            items.append(item)
        triangle.append(items)
    return triangle

def print_pascal_triangle(levels=10):
    triangle = pascal_triangle(levels)
    blocks = len(str([str(item) for item in triangle[-1]])) + len(triangle[-1])
    for i in range(levels):
        array = triangle[i]
        array = [str(item) for item in array]
        content_str = ' '.join(array)
        empty_str = (blocks - len(content_str))//2
        print(empty_str*' ' + content_str)
    return

if __name__ == "__main__":
    print_pascal_triangle(10)

def print_pyramid(levels = 10):
    blocks = 2*levels - 1
    for i in range(1, levels+1):
        filled_blocks = 2*i - 1
        empty_blocks = (blocks-filled_blocks)//2
        print(empty_blocks*' ',filled_blocks*'*',empty_blocks*' ','\n')
    return

if __name__ == "__main__":
    print_pyramid(100)

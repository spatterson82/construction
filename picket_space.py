import sys


def get_picket_spacing(total_distance, num_of_pickets=2, picket_width=1.5):
    min_spacing = 3.0
    spacing = 3.1
    while spacing > min_spacing:
        empty_space = total_distance - (num_of_pickets * picket_width)
        spacing = empty_space / (num_of_pickets - 1)
        num_of_pickets += 1
        if spacing > 4:
            continue
        else:
            print('pickets:', num_of_pickets - 1)
            print('spacing:', str(spacing) + "\n")


if __name__ == "__main__":
    cedar_blocks = 5
    total_distance = float(sys.argv[1]) - cedar_blocks
    get_picket_spacing(total_distance)
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
            remainder = spacing % 1
            eighths = int(remainder / .06125)
            print('\npickets:', num_of_pickets - 1)
            print(f'spacing: {str(int(spacing))} and {eighths}/16"')


if __name__ == "__main__":
    cedar_blocks = 5
    total_distance = float(input('Distance between posts:'))
    get_picket_spacing(total_distance)
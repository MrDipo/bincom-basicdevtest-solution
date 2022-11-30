import random

WEEK = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN".split(", "),
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE".split(", "),
    "WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE".split(", "),
    "THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN".split(", "),
    "FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE".split(", ")
}

COLOR_VALUES = {
    'ARSH' : 1,
    'BLACK': 2,
    'BLEW': 3,
    'BLUE': 4,
    'BROWN': 5,
    'CREAM': 6,
    'GREEN': 7,
    'ORANGE': 8,
    'PINK': 9,
    'RED' : 10,
    'WHITE' : 11,
    'YELLOW' : 12
}

COLORS = []
for value in WEEK.values():
    COLORS += value
COLORS.sort()

def mean_color(colors=COLORS, color_values=COLOR_VALUES):
    sum = 0
    for color in colors:
        sum += color_values[color]
    mean = sum//len(colors)
    for key, value in color_values.items():
        if mean == value:
            return f"The mean colour is {key}"


def mode_color(week):
    pass

def median_color(week):
    pass

def variance_color(week):
    pass

def probability_color(week, color):
    pass

def save_to_db(color_freq):
    pass

def binary_search(n, nums):
    nums.sort()
    def recursive(left, right):
        if left <= right:
            middle = (left + right) // 2
            if nums[middle] == n:
                return True
            if nums[middle] < n:
                return recursive(middle + 1, right)
            elif nums[middle] > n:
                return recursive(left, middle - 1)
        return False
    return recursive(0, len(nums) - 1)


def num_generator():
    base2_num = ""
    for i in range(4):
        temp = str(random.randint(0,1))
        base2_num += temp
    base10_num = int(base2_num, 2)
    return f"Binary number generated: {base2_num}, Decimal Equivalent: {base10_num}"
    

def fib(n=50):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1)+fib(n-2)

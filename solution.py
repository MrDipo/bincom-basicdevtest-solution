import random, statistics, psycopg2

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


def mode_color(colors=COLORS):
    return f"Most common color is {statistics.multimode(colors)}"


def median_color(colors=COLORS):
    return f"Median color is {statistics.median(colors)}"


def variance_color(colors=COLORS, color_values=COLOR_VALUES):
    sum = 0
    squared_diff_sum = 0
    for color in colors:
        sum += color_values[color]
    mean = sum/len(colors)
    for color in colors:
        squared_diff_sum += (color_values[color] - mean)**2
    variance = squared_diff_sum/len(colors)
    return variance


def probability_color(colors=COLORS, color='RED'):
    return f"Probability of {color} being chosen is {round(colors.count(color)/len(colors), 3)}"


def save_to_db(colors=COLORS, color_value=COLOR_VALUES):
    def create_table():
        conn = psycopg2.connect("dbname='colors' user='postgres' password='0000' host='localhost' port='5432'")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS colors (color TEXT, frequency INTEGER)")
        conn.commit()
        conn.close()

    def insert(color, frequency):
        conn = psycopg2.connect("dbname='colors' user='postgres' password='0000' host='localhost' port='5432'")
        cur = conn.cursor()
        cur.execute("INSERT INTO colors VALUES(%s,%s)", (color,frequency))
        conn.commit()
        conn.close()

    def view():
        conn = psycopg2.connect("dbname='colors' user='postgres' password='0000' host='localhost' port='5432'")
        cur = conn.cursor()
        cur.execute("SELECT * FROM colors")
        rows = cur.fetchall()
        conn.close()
        return rows
    
    create_table()
    for color in color_value.keys():
        insert(color, colors.count(color))
    return view()


def binary_search(n=69, nums=[1,2,3,4,7,3,2,4,6,9,43,23,554,65,123,78,9,6345,235,465,3123,69]):
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
    
cache = {0:0, 1:1}
def fib(n):
    if n in cache: # base case
        return cache[n]
    # Compute and cache the Fibonacci number
    cache[n] = fib(n - 1) + fib(n - 2)  # Recursive case
    return cache[n]
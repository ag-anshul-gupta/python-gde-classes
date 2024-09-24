def x_or_y(x, y):
    if x > y:
        print("big")
    else:
        print("small")

def run_loop(count = 5):
    for i in range(count):
        print(i)

def get_season_name(season_number):
    if season_number == 1:
        return "summer"
    elif season_number == 2:
        return "winter"
    elif season_number == 3:
        return "fall"
    else:
        return "spring"

def print_pattern(size):
    for i in range(1, size + 1):
        for j in range(i):
            print("*", end=" ")
        print()
#print_pattern(5)

def print_x(n):
    for i in range(n):
        start = i
        end = n - i - 1
        if start > end:
            end, start = start, end
        space = end - start + 1
        if start == end:
            print(" " * (start + 2) , "*", end="")
        else:
            print(" " * start, "*", " " * space, "*", end="")
        print()
def calculate_sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

print_x(9)



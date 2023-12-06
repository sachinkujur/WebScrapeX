import math


def calculate_and_round_series(start, end):
    last_rounded_result = None
    change_points = []

    for num in range(start, end + 1):
        result = num * 0.002  # 0.2% is equivalent to 0.002
        rounded_result = math.floor(result)

        if rounded_result != last_rounded_result:
            change_points.append((num, rounded_result))
            last_rounded_result = rounded_result

    return change_points


# Example usage
start_number = int(input("Enter the start number: "))
end_number = int(input("Enter the end number: "))
change_points = calculate_and_round_series(start_number, end_number)

print(f"Change points in the number series from {start_number} to {end_number}:")
for point in change_points:
    num, rounded_result = point
    print(f"At {num}, the rounded result changes to {rounded_result}")

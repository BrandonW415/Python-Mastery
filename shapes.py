from typing import Callable, Dict, Tuple
import math

def rectangle_area(length: float, width: float) -> float:
    return length * width

def circle_area(radius: float) -> float:
    return math.pi * radius ** 2

def triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

def square_perimeter(side_length: float) -> float:
    return 4 * side_length

def circle_circumference(radius: float) -> float:
    return 2 * math.pi * radius

def circle_details(radius: float) -> Tuple[float, float]:
    return circle_circumference(radius), circle_area(radius)

def compare_shapes(shape1_name: str, shape1_value: float, shape2_name: str, shape2_value: float, comparison_type: str) -> str:
    if shape1_value > shape2_value:
        return f"The {shape1_name} has a larger {comparison_type}."
    elif shape1_value < shape2_value:
        return f"The {shape2_name} has a larger {comparison_type}."
    else:
        return f"The {shape1_name} and {shape2_name} have equal {comparison_type}s."

def geometry(square_side: float, circle_radius: float) -> None:
    square_perim = square_perimeter(square_side)
    circle_circum = circle_circumference(circle_radius)
    
    square_area = square_side ** 2
    circle_area_val = circle_area(circle_radius)
    
    print(f"Square side length: {square_side}")
    print(f"Circle radius: {circle_radius}")
    print()
    
    print(compare_shapes("square", square_perim, "circle", circle_circum, "perimeter/circumference"))
    print(compare_shapes("square", square_area, "circle", circle_area_val, "area"))

def get_float_input(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be positive")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive number.")

def print_result(shape: str, measurement: str, value: float) -> None:
    print(f"The {measurement} of the {shape} is: {value:.2f}")

def create_options() -> Dict[str, Tuple[str, Callable[[], None]]]:
    return {
        "1": ("rectangle area", lambda: print_result("rectangle", "area", rectangle_area(
            get_float_input("Enter the length of the rectangle: "),
            get_float_input("Enter the width of the rectangle: ")))),
        "2": ("circle area", lambda: print_result("circle", "area", circle_area(
            get_float_input("Enter the radius of the circle: ")))),
        "3": ("triangle area", lambda: print_result("triangle", "area", triangle_area(
            get_float_input("Enter the base of the triangle: "),
            get_float_input("Enter the height of the triangle: ")))),
        "4": ("square perimeter", lambda: print_result("square", "perimeter", square_perimeter(
            get_float_input("Enter the side length of the square: ")))),
        "5": ("circle details", lambda: (lambda r: print(f"Circle with radius {r}:\n"
            f"Circumference: {circle_circumference(r):.2f}\n"
            f"Area: {circle_area(r):.2f}"))(get_float_input("Enter the radius of the circle: "))),
        "6": ("compare square and circle", lambda: geometry(
            get_float_input("Enter the side length of the square: "),
            get_float_input("Enter the radius of the circle: "))),
        "7": ("exit", lambda: print("Thank you for using the Geometry Calculator. Goodbye!"))
    }

def main() -> None:
    options = create_options()

    while True:
        print("\nGeometry Calculator")
        for key, (description, _) in options.items():
            print(f"{key}. {description.capitalize()}")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice in options:
            options[choice][1]()
            if choice == "7":
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
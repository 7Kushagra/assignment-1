def print_lower_triangular(rows, char="*"):
   
    print(f"Lower Triangular ({rows} rows) ")
    for i in range(1, rows + 1):
        print(char * i)
    print("-" * 30)
def print_upper_triangular (rows, char="*"):
    print(f"Upper Triangular ({rows} rows) ")
    for i in range(rows, 0, -1):
        print(char * i)
    print("-" * 30)
def print_pyramid(rows, char="*"):
   
    print(f"Pyramid ({rows} rows)")
    for i in range(1, rows + 1):
        
        spaces_count = rows - i
       
        stars_count = (2 * i) - 1

        print(" " * spaces_count + char * stars_count)
    print("-" * 30)

if __name__ == "__main__":
    while True:
        try:
            num_rows = int(input("Enter the number of rows for the triangles (e.g., 5): "))
            if num_rows > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print("\n")
    print_lower_triangular(num_rows)
    print_upper_triangular(num_rows)
    print_pyramid(num_rows)
    print("\nAll patterns printed!")

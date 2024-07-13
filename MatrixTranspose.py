def transpose_matrix():
    """
    Compute the transpose of a matrix entered by the user.

    Returns:
    - list of lists: The transpose of the input matrix.
    """
    # Prompt the user for matrix dimensions
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Initialize the matrix based on user input
    matrix = []
    print("Enter the elements row-wise:")

    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    # transpose of the matrix
    transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    return matrix, transpose

original_matrix, transposed_matrix = transpose_matrix()

print("Original Matrix:")
for row in original_matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)

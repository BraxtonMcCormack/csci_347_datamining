def one_hot_encoding(data):
    """Transform categorical attributes in data to one-hot encoding."""
    # Create unique value mapping for each attribute
    colors = {v: i for i, v in enumerate(sorted(set(row[0] for row in data)))}      #for future hw where I might use this, future me you probally only need to adjust/modify these three lines maybe change their names
    yes_no = {v: i for i, v in enumerate(sorted(set(row[1] for row in data)))}
    directions = {v: i for i, v in enumerate(sorted(set(row[2] for row in data)))}

    # Encode data
    transformed_data = []
    for row in data:
        encoded_row = [0] * (len(colors) + len(yes_no) + len(directions))
        encoded_row[colors[row[0]]] = 1
        encoded_row[len(colors) + yes_no[row[1]]] = 1
        encoded_row[len(colors) + len(yes_no) + directions[row[2]]] = 1
        transformed_data.append(encoded_row)
    return transformed_data

def euclidean_distance(row1, row2):
    """Calculate the Euclidean distance between two data rows."""
    return sum((a - b) ** 2 for a, b in zip(row1, row2)) ** 0.5

def cosine_similarity(row1, row2):
    """Calculate the cosine similarity between two data rows."""
    dot_product = lambda v1, v2: sum(a*b for a, b in zip(v1, v2))
    magnitude = lambda v: dot_product(v, v) ** 0.5
    return dot_product(row1, row2) / (magnitude(row1) * magnitude(row2))

def hamming_distance(row1, row2):
    """Calculate the Hamming distance between two data rows."""
    return sum(a != b for a, b in zip(row1, row2))

def jaccard_coefficient(row1, row2):
    """Calculate the Jaccard coefficient between two binary data rows."""
    intersection = sum(a == b and a == 1 for a, b in zip(row1, row2))
    union = sum(a == 1 or b == 1 for a, b in zip(row1, row2))
    return intersection / union

def multivariate_mean(data):
    """Calculate the multivariate mean of a dataset."""
    return [sum(col) / len(data) for col in zip(*data)]

def sample_variance(column):
    """Calculate the sample variance of a single data column."""
    mean = sum(column) / len(column)
    return sum((x - mean) ** 2 for x in column) / (len(column) - 1)

def z_score_normalization(data):
    """Normalize dataset using Z-score normalization."""
    means = multivariate_mean(data)
    std_devs = [sample_variance(col) ** 0.5 for col in zip(*data)]
    normalized_data = []
    for row in data:
        normalized_row = [(val - mean) / std if std else 0 for val, mean, std in zip(row, means, std_devs)]
        normalized_data.append(normalized_row)
    return normalized_data

def print_rounded_array(arr, precision=3):
    """
    Prints each sub-array on a new line with rounded values to the specified precision.
    
    Parameters:
    - arr: A list of lists (2D array) with float values.
    - precision: The number of decimal places to round to. Default is 3.
    """
    # Iterating over each sub-array
    for sub_arr in arr:
        # Rounding each value in the sub-array to the specified precision and converting to string
        rounded_sub_arr = [f"{x:.{precision}f}" for x in sub_arr]
        # Joining the rounded values with a space and printing the result
        print(" ".join(rounded_sub_arr))
    print("\n")


# Define the data matrix from the PDF
data = [
    ("red", "yes", "North"),
    ("blue", "no", "South"),
    ("yellow", "no", "East"),
    ("yellow", "no", "West"),
    ("red", "yes", "North"),
    ("yellow", "yes", "North"),
    ("blue", "no", "West")
]

# Applying one-hot encoding to transform the data matrix
matrix_y = one_hot_encoding(data)
# print("Q1: One Hot Encoded Matrix Y: ", matrix_y, "\n")
print("Q1: One Hot Encoded Matrix Y: ")
print_rounded_array(matrix_y, 0)

# Calculate the Euclidean distance between x2 and x7 after one-hot encoding
euclidean_distance_x2_x7 = euclidean_distance(matrix_y[1], matrix_y[6])
print("Q2: Euclidean distance between x2 and x7: ", euclidean_distance_x2_x7, "\n")

# Calculate the cosine similarity between x2 and x7 after one-hot encoding
cosine_similarity_x2_x7 = cosine_similarity(matrix_y[1], matrix_y[6])
print("Q3: cosine similarity between x2 and x7: ", cosine_similarity_x2_x7, "\n")

# Calculate the Hamming distance between x2 and x7
hamming_distance_x2_x7 = hamming_distance(matrix_y[1], matrix_y[6])
print("Q4: Hamming distance between x2 and x7: ", hamming_distance_x2_x7, "\n")

# Calculate the Jaccard coefficient between x2 and x7 after one-hot encoding
jaccard_coefficient_x2_x7 = jaccard_coefficient(matrix_y[1], matrix_y[6])
print("Q5: Jaccard coefficient between x2 and x7: ", jaccard_coefficient_x2_x7, "\n")

# Calculate the multivariate mean of Y
mean_Y = multivariate_mean(matrix_y)
print("Q6: multivariate mean of Y: ", mean_Y, "\n")

# Calculate the sample variance of the first column of Y
variance_first_column_Y = sample_variance([row[0] for row in matrix_y])
print("Q7: sample variance of the first column of Y: ", variance_first_column_Y, "\n")

# Apply Z-score normalization to Y
Z = z_score_normalization(matrix_y)
# print("Q8: Z-score normalization of Y: ", Z, "\n")
print("Q8: Z-score normalization of Y:")
print_rounded_array(Z)

# Calculate the multivariate mean of Z
mean_Z = multivariate_mean(Z)
print("Q9: multivariate mean of Z: ", mean_Z, "\n")

# Calculate the Euclidean distance between z2 and z7
euclidean_distance_z2_z7 = euclidean_distance(Z[1], Z[6])
print("Q10: Euclidean distance between x2 and x7: ", euclidean_distance_z2_z7, "\n")








# X1 = ["red", "blue", "yellow", "yellow", "red", "yellow", "blue"]
# X2 = ["yes", "no", "no", "no", "yes", "yes", "no"]
# X3 = ["North", "South", "East", "West", "North", "North", "West"]
def sample_mean(data):
    """Calculate the sample mean of a list of numbers."""
    return sum(data) / len(data)

def sample_variance(data):
    """Calculate the sample variance of a list of numbers."""
    mean = sample_mean(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)

def sample_covariance(data1, data2):
    """Calculate the sample covariance between two lists of numbers."""
    mean1 = sample_mean(data1)
    mean2 = sample_mean(data2)
    return sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2)) / (len(data1) - 1)      #this is kinda really neat https://www.w3schools.com/python/ref_func_zip.asp

def multivariate_sample_mean(*data_sets):
    """Calculate the multivariate sample mean of multiple lists of numbers."""
    means = [sample_mean(data) for data in data_sets]
    return means

def covariance_matrix(*data_sets):
    """Calculate the covariance matrix for multiple lists of numbers."""
    n = len(data_sets)
    cov_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            cov = sample_covariance(data_sets[i], data_sets[j])
            cov_matrix[i][j] = cov
            cov_matrix[j][i] = cov

    return cov_matrix

def correlation(data1, data2):
    """Calculate the correlation between two lists of numbers."""
    cov = sample_covariance(data1, data2)
    std_dev1 = sample_variance(data1) ** 0.5
    std_dev2 = sample_variance(data2) ** 0.5
    return cov / (std_dev1 * std_dev2)

def total_variance(cov_matrix):
    """Calculate the total variance from a covariance matrix."""
    return sum(cov_matrix[i][i] for i in range(len(cov_matrix)))

X1 = [0.3, 0.4, 1.8, 6, -0.5, 0.4, 1.1]
X2 = [23, 1, 4, 50, 34, 19, 11]
X3 = [5.6, 5.2, 5.2, 5.1, 5.7, 5.4, 5.5]

mean = sample_mean(X3)
print("Sample Mean: " + str(mean))

cov = sample_covariance(X1, X3)
print("Sample Covariance: " + str(cov))

multivariate_mean = multivariate_sample_mean(X1, X2, X3)
print("Multivariate Sample Mean: " + str(multivariate_mean))

variance = sample_variance(X2)
print("Sample Variance of (sigma Hat Squared): " + str(variance))

cov_mat = covariance_matrix(X1, X2, X3)
print("Covariance matrix : " + str(cov_mat))

corr = correlation(X1, X3)
print("Correlation between X1 and X3: " + str(corr))

total_var = total_variance(cov_mat)
print("Total Variance: " + str(total_var))


print("\n\n\n")

'''Question 3 code now'''

def l2_norm(vector):
    """Calculate the L2 norm (Euclidean distance) of a vector."""
    return sum(x ** 2 for x in vector) ** 0.5

def l1_norm(vector):
    """Calculate the L1 norm (Manhattan distance) of a vector."""
    return sum(abs(x) for x in vector)

def cosine_of_angle(a, b):
    """Calculate the cosine of the angle between two vectors."""
    dot_product = sum(x * y for x, y in zip(a, b))
    norm_a = l2_norm(a)
    norm_b = l2_norm(b)
    return dot_product / (norm_a * norm_b)

a = (2, 5, -2.6, 6)
b = (15, 2.5, 4, 4)

# Calculate the L2 norm of the difference between vectors a and b
l2_norm_diff = l2_norm([ai - bi for ai, bi in zip(a, b)])
print("L2 Norm of the difference: " + str(l2_norm_diff))

# Calculate the L1 norm of the difference between vectors a and b
l1_norm_diff = l1_norm([ai - bi for ai, bi in zip(a, b)])
print("L1 Norm of the difference: " + str(l1_norm_diff))

# Calculate the cosine of the angle between vectors a and b
cosine_angle = cosine_of_angle(a, b)
print("Cosine of the angle: " + str(cosine_angle))
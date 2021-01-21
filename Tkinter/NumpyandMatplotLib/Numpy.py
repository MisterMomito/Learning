import numpy as np

x = [1, 2, 3.5, 4.8]
a = np.array(x)
print(a, end='\n\n')
print(a*2, end='\n\n')  # multiplies everything by 2

x = np.arange(1, 10)  # generates a np array of values 1-9
print(x, end='\n\n')
print(np.arange(0.1, 1.2, 0.1), end='\n\n')  # start, end(exclusive), gap

# multi-dimensional np array
b = np.array([[1, 1], [2, 2]])
print(b)
print('Dimensions: ' + str(b.ndim))  # .ndim checks dimensions
print('Shape: ' + str(np.shape(b)), end='\n\n')  # checks shape

# indexing works the same as regular python indexing
print(b[0])

# generating random numbers

c = np.random.randn(6, 4)
print(c)

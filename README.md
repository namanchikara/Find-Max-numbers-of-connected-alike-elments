# Find-Max-numbers-of-connected-alike-elments

Given a N x M 2D array of various values (repeatable), this program will return maximum value of connected components with same values.

For example:

We have an array of 5 rows and (M) columns in each row (Program is flexible so that M can vary, i.e for each row-> number of columns could vary.


1 0 1 2 2 2 2 1 1

1 0 1 1 2 2

1 1 1 2 2 2 2 1


Maximum connected element in above matrix is 2, with 10 values, so the program will return 10 on executing FindMaxNow() and will return 2 on executing FindMaxElement() on the object of FindMax class.

If there are two elements with same connected components then it will return a list of such components for example:

1 1 1

2 2 2

1 1 1


on executing FindMaxElement(), function will return [1,2,1].
Whereas, on exeuting FindMaxNow() will return 3

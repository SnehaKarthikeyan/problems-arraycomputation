# problems-arraycomputation

Question:

Given a number N, array of N integers and an integer k. Write a program to print the resultant values after multiplying consecutive pair elements of the given array. 
Input Size : |N| <= 1000000

Input Description:

The first line contains an integer N. The second line contains N space-separated integers, which denotes array elements.

Output Description:

Print the resultant values separated by a space after multiplying consecutive pair elements of the given array

Hints:

Multiply consecutive pair elements of the given array

Sample Input:

4\n
1 6 2 9 

Sample Output:

6 12 18

Explanation:

After multiplying consecutive pair elements of the given array (1*6, 6*2 and 2*9), the resultant array is 6 12 18

Testcase 1:

Input:

40\n 
34 56 78 67 22 43 54 66 23 45 68 11 25 45 55 67 11 73 67 34 56 78 87 67 23 45 68 11 25 45 55 67 11 73 67 34 56 78 67 22

Output:

1904 4368 5226 1474 946 2322 3564 1518 1035 3060 748 275 1125 2475 3685 737 803 4891 2278 1904 4368 6786 5829 1541 1035 3060 748 275 1125 2475 3685 737 803 4891 2278 1904 4368 5226 1474

Testcase 2:

Input:

22\n 
45 78 93 22 45 23 56 79 99 54 51 12 34 43 34 78 66 32 44 35 67 29

Output:

3510 7254 2046 990 1035 1288 4424 7821 5346 2754 612 408 1462 1462 2652 5148 2112 1408 1540 2345 1943

Testcase 3:

Input:

15\n
56 32 43 11 78 33 11 23 89 33 12 45 78 23 66

Output:

1792 1376 473 858 2574 363 253 2047 2937 396 540 3510 1794 1518

Testcase 4:

Input:

38\n
11 78 33 11 23 89 33 12 45 23 56 79 99 54 51 12 34 43 34 78 66 32 44 35 45 78 23 66 34 56 78 87 67 23 45 68 11 25

Output:

858 2574 363 253 2047 2937 396 540 1035 1288 4424 7821 5346 2754 612 408 1462 1462 2652 5148 2112 1408 1540 1575 3510 1794 1518 2244 1904 4368 6786 5829 1541 1035 3060 748 275

Testcase 5:

Input:

47\n
11 23 89 33 12 45 78 23 66 11 78 33 11 23 89 33 12 45 23 56 79 99 54 51 12 34 43 34 78 66 32 44 35 45 78 23 66 34 56 78 87 67 23 45 68 11 25

Output:

253 2047 2937 396 540 3510 1794 1518 726 858 2574 363 253 2047 2937 396 540 1035 1288 4424 7821 5346 2754 612 408 1462 1462 2652 5148 2112 1408 1540 1575 3510 1794 1518 2244 1904 4368 6786 5829 1541 1035 3060 748 275

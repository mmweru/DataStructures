# # # # # # # values = [8, 3, 5, 1, 9, 4]
# # # # # # # if __name__ == '__main__':
# # # # # # # n = int(input())
# # # # # # # arr = map(int, input().split())
# # # # # # #
# # # # # # # sort = sorted(arr)
# # # # # # #
# # # # # # # for i in sort:
# # # # # # #     print(sort[-2])
# # # # # # students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# # # # # #
# # # # # # students = sorted(students)
# # # # # # print(students)
# # # # # # for _ in range(int(input())):
# # # # # #         name = input()
# # # # # #         score = float(input())
# # # # # #         my_list = []
# # # # # #         my_list.append([name, score])
# # # # # #
# # # # # #
# # # # # # length = len(students)
# # # # # # i = 0
# # # # # # second = 0
# # # # # # elements = []
# # # # # # while i < len(students):
# # # # # #     elements.append(students[i][1])
# # # # # #     i += 1
# # # # # # sort = sorted(elements)
# # # # # # a = 0
# # # # # # for i in range(a+1, len(sort)):
# # # # # #     if sort[a] < sort[i]:
# # # # # #         second = sort[i]
# # # # # #         break
# # # # # #     i += 1
# # # # # # for i in range(len(students)):
# # # # # #     if second == students[i][1]:
# # # # # #         print(students[i][0])
# # # # # #     i += 1
# # # # # #
# # # # # # print(second)
# # # # # # print(elements)
# # # # # # print(sort)
# # # # # #
# # # # # #
# # # # # #
# # # # # # # for i in students:
# # # # # # #     print(students[0][1])
# # # # # # #     break
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # # pivot = values[len(values)-1]
# # # # # # # j = 0
# # # # # # # i = 0
# # # # # # # sorted = True
# # # # # # #
# # # # # # # while sorted:
# # # # # # #     for value in range(0, len(values) - 1):
# # # # # # #         if values[value] < values[value + 1]:
# # # # # # #             temp = values[value]
# # # # # # #             values[value] = values[value + 1]
# # # # # # #             values[value + 1] = temp
# # # # # # # print(values)
# # # # # # # large = 0
# # # # # # # for i in range(len(values) - 1):
# # # # # # #     if values[i] > values[i + 1]:
# # # # # # #         large = values[i]
# # # # # # #     i += 1
# # # # # # #
# # # # # # # print(large)
# # # # # #
# # # # # # # while i < len(values):
# # # # # # #     while i == 0:
# # # # # # #         if values[i] < pivot:
# # # # # # #             temp = values[i]
# # # # # # #             values[i] = pivot
# # # # # # #             pivot = temp
# # # # # # #     if values[i + 1] < pivot:
# # # # # # #         temp = values[j]
# # # # # # #         values[j] = values[i]
# # # # # # #         values[i] = temp
# # # # # # #     print(values)
# # # # # #
# # # # #
# # # # # list = {'alpha': [20, 30, 40], 'beta': [30, 50, 77]}
# # # # # query_name = 'beta'
# # # # # average = 0
# # # # # sum = 0
# # # # #
# # # # # for i in list.keys():
# # # # #     if query_name in i:
# # # # #         for value in list[query_name]:
# # # # #             sum += value
# # # # #             average = sum / len(list[query_name])
# # # # #
# # # # # print(round(average, 2))
# # # #
# # # # string = "ABCDCDC"
# # # # sub = "CDC"
# # # # count = 0
# # # # size = len(sub)
# # # # for i in range(len(string)):
# # # #     if sub in string[i: i+size]:
# # # #         count += 1
# # # #     i += 1
# # # # print(count)
# # #
# # # S = "qA2"
# # #
# # # # for i in S:
# # #
# # #     # print(True) if i.isalpha() else print(False)
# # #     # if i.isalnum():
# # #     #     print(True)
# # #     #     break
# # #     # else:
# # #     #     print(False)
# # #     # if i.isalpha():
# # #     #     print(True)
# # #     #     continue
# # #     # else:
# # #     #     print(False)
# # #
# # # # print(True) if S.__contains__() else print(False)
# # # # print(True) if S.isalpha() else print(False)
# # # # print(True) if S.isdigit() else print(False)
# # # # print(True) if S.islower() else print(False)
# # # # print("Hello World")
# # # # print(True) if S.isupper() else print(False)
# # #
# # # a = [1, 2, 3]
# # # b = [3, 2, 1]
# # # alice = 0
# # # bob = 0
# # # for i in range(len(a)):
# # #     if a[i] > b[i]:
# # #         alice += 1
# # #     elif b[i] > a[i]:
# # #         bob += 1
# # #     i += 1
# # # print("Alice's {}".format(alice))
# # # print("Bob's {}".format(bob))
# # #
# # # sum1 = 0
# # # sum2 = 0
# # # n = 3
# # # i = 0
# # # j = n - 1
# # # arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
# # # for i in range(i, n):
# # #     sum1 += arr[i][i]
# # # while n > 0:
# # #     for i in range(i, n):
# # #         sum2 += arr[i][n - 1]
# # #         n -= 1
# # #
# # # # abs = sum1 - sum2
# # # # if abs == -(abs):
# # # #     print(-1*(abs))
# # # # else:
# # # #     print(abs)
# #
# # # S = "ababccca"
# # # S1 = "ab"
# # # S2 = "c"
# #
# # # count1 = 0
# # # size = len(S1)
# # # size2 = len(S2)
# # # for i in range(N % 998244353):
# # #     if S1 in M[i: i+size]:
# # #         count += 1
# # #     elif S2 in M[i: i+size2]:
# # #         count1 += 1
# # #     i += 1
# # # sum = count + count1
# # # print(sum)
# # #
# # # def output(M, S):
# # #     count = 0
# # #     for j in range(M):
# # #         for i in range(len(S) % 998244353):
# # #             if S[j] in S[i: i + len(S[j])]:
# # #                 count += 1
# # #             i += 1
# # #         j += 1
# # #     return(count)
# # #
# # # M = 2
# # # S = "ababccca"
# # # print(output(M, S))
# #
# # # You are given an integer N, followed by N lines of input (1 <= N <= 100). Each line of input contains one number M.
# # #
# # # Write a program that goes through the numbers from 1 to M (1 <= M <= 100) and prints out the following:
# # #
# # # For numbers which are multiples of three print "Ona".
# # # For numbers which are the multiples of five print "Data".
# # # For numbers which are multiples of both three and five print "OnaData".
# # # If the conditions above fail for all numbers, print "N/A".
# # N = 3
# # M = 2
# # Si = "ababccca"
# # count = 0
# # j = 0
# # for j in range(M):
# #     for i in range(N % 998244353):
# #         if M[j] in Si[i: )]:
# #             count += 1
# #         i += 1
# #     j += 1
# # print(count)
# # N = len("ababccca")
# # M = 1
# # count = 0
# # msg = ""
# # S = "ababccca"
# # j = 0
# # for j in range(M):
# #     msg = "ab"
# #     for i in range(N % 998244353):
# #         if msg in S[i: i+len(msg)]:
# #             count += 1
# #         i += 1
# #     j += 1
# # print(count)
# # def my_value(N, M):
# #     count = 0
# #     S = "ababccca"
# #     S = S[:N]
# #     for j in range(0, M):
# #         msg = input("")
# #         for i in range(N % 998244353):
# #             if msg in S[i: i + len(msg)]:
# #                 count += 1
# #             i += 1
# #         j += 1
# #     return (2 ** count)
# #
# # N, M= input("").split()
# # print(my_value(int(N), int(M)))
# # n = input("")
# # size = len(n)
# count = 0
# z = 23
# while z != '\0':
#
# # while z <= 44:
# #     if z <= 10:
# #         if z == 1 or z == 10:
# #             count += 1
# #         else:
# #             count += 0
# #     elif z > 10:
# #         a = z // 10
# #         b = z % 10
# #         s = ((a ** 2) + (b ** 2))
# #         while s >= 10:
# #             a = s // 10
# #             b = s % 10
# #             print("still in the loop")
# #             s = ((a ** 2) + (b ** 2))
# #         if s == 1:
# #
# #             count += 1
# #     z += 1
# # print(count)
#
#
#     # for i in range(0, len(str(z))):
#     #     n = str(z)
#     #     one = (int(n[i]) * int(n[i]))
#     #     sum += one
# #         checker = len(str(sum))
# #         num = str(sum)
# #         for i in range(0, len(num)):
# #             new = (int(num[i]) * int(num[i]))
# #             n_size += new
# #             checker = len(str(n_size))
# #             if checker > 1:
# #                 new = (int(num[i]) * int(num[i]))
# #                 n_size += new
# #             else:
# #                 if n_size == 1:
# #                     count += 1
# #
# #     z += 1
# # print(count)
# # #
# #
# # count = 0
# # for i in range(0, len(num)):
# #     #print(num[i])
# #     new = (int(num[i]) * int(num[i]))
# #     n_size += new
# #     checker = len(str(n_size))
# #     if checker > 1:
# #         new = (int(num[i]) * int(num[i]))
# #         n_size += new
# #     else:
# #         if n_size == 1:
# #             count += 1
# #
# #
# #
# # print(count)
#
#
#     # sum = int(i) * int(i)
#     # sum = str(sum)
#     # n_size = len(sum)
#     # temp = size
#     # size = n_size
#
#
# #print(size)
#
#
#
#
#

# import sys
#
# largest_number = -sys.maxsize
# for i in range(3):
#     number = int(input())
#     if number > largest_number:
#         largest_number = number
# print(largest_number)


numbers = [int(input()) for x in range(3)]
print(max(numbers))

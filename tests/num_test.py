# def plus(num):
#     eq = (num + 3) * 2
#     return eq
#
# if __name__ == "__num_test__":
#     print(plus(5))

#=======================================================



# def print6(xs):
#     for i, x in enumerate(xs):
#         print(x)
#         if i == 5:
#             break
#
#
# i = (x * x for x in range(10))
#
# print(print6(i))

#=======================================================

# cube = list((x**3 for x in range(10) if x % 2 == 0))
#
# print(cube)

#=======================================================

# def summ_numbes(numbers_list):
#     return sum(x**2 for x in numbers_list if x >0)
#
# print(summ_numbes([1,2,3,4,5,-4,6,-3]))
#
# print(list(x*2 for x in [1,2,3,4,5,-4,6,-3]))

#=======================================================

gl_words = (x for x in 'hello' if x in ['a', 'a', 'a', 'a', 'a',])

print(*(x for x in "Hello World!" if x.isupper()))

#=======================================================



#=======================================================



#=======================================================
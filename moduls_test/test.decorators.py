from src.decorators import decor_log as decor


#@decor(filename="log_decorators.txt")
@decor()
def func_test(x, y):
    result = int(x) / int(y)
    return result


print("Давайте разделим два числа")
us_in_x = input("Write first number: ")
us_in_y = input("Write second number: ")
print(f"Ответ: {func_test(us_in_x, us_in_y)}")

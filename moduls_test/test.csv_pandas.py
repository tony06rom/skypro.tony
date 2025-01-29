from src.csv_pandas import csv_worker, excel_worker

print("--- 13.1 Библиотеки csv и pandas ---")

# Тест функции csv_worker
input_csv_file = input(
    "===> Введите путь и имя csv файла в формате '../path/path/file_name', где:\n"
    "===> .. - корневой каталог\n===> path - директория\\папка\n"
    "===> file_name - имя файла (с расширением)\n===> Ввод: "
)
if input_csv_file == "":
    print(csv_worker())
else:
    print(csv_worker(input_csv_file))
print("===========================")
answer_user = str(input("===> Хотите продолжить? [да(yes)/нет(no)]\n"))
list_answers_yes = ["да", "y", "yes"]
list_answers_no = ["нет", "n", "no"]
if answer_user.lower() in list_answers_yes:
    print("===========================")
    # Тест функции excel_worker
    input_excel_file = input(
        "===> Введите путь и имя excel файла в формате '../path/path/file_name', где:\n"
        "===> .. - корневой каталог\n===> path - директория\\папка\n"
        "===> file_name - имя файла (с расширением)\n===> Ввод: "
    )
    if input_excel_file == "":
        print(excel_worker())
    else:
        print(excel_worker(input_excel_file))
else:
    print("До свидания!")

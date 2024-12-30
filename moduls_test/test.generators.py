from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions


# Тест функции filter_by_currency
def uniq_code(start_data):
    currency_code = []
    for data in start_data:
        if data["operationAmount"]["currency"]["code"] not in currency_code:
            currency_code.append(data["operationAmount"]["currency"]["code"])
    return "\n".join(currency_code)


def count_code(start_data, user_input):
    count = 0
    for data in start_data:
        if data["operationAmount"]["currency"]["code"] == user_input:
            count =+ 1
    return count


input_user = str(input(f"===> Введите одно из допустимых значений currency_code:\n{uniq_code(transactions)}\n"))
print(f"===> Транзакции по фильтру currency_code = {input_user}:")
print("===========================")
usd_transactions = filter_by_currency(transactions, input_user)
for i in range(count_code(transactions,input_user) + 1):
    next_transact = input("===> Введите Enter для вывода транзакции ")
    print(next(usd_transactions))
print("===> Все транзакции были выведены\n===========================")


# Тест функции transaction_descriptions
descriptions = transaction_descriptions(transactions)
for i in range(len(transactions)):
    next_transact = input("===> Введите Enter для вывода информации по транзакции")
    print(next(descriptions))
print("===> Вся информация по типа транзакций была выведена")


# Тест функции card_number_generator
start_input = int(input("===========================\n===> Введите начальный диапазон номеров карт: "))
end_input = int(input("===> Введите конечный диапазон номеров карт: "))
print("===========================\n===> Номера карт")
for card_number in card_number_generator(start_input, end_input):
    print(card_number)
print("===> Все номера карт были сгенерированы")

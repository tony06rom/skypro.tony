from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions


# Тест функции filter_by_currency
def uniq_code(start_data):
    currency_code = []
    for data in start_data:
        if data["operationAmount"]["currency"]["code"] not in currency_code:
            currency_code.append(data["operationAmount"]["currency"]["code"])
    return "\n".join(currency_code)


input_user = str(input(f"Введите одно из допустимых значений currency_code:\n{uniq_code(transactions)}\n"))
print(f"Транзакции по фильтру currency_code = {input_user}:")
print("===========================")
usd_transactions = filter_by_currency(transactions, input_user)
for i in range(2):
    next_transact = input("Введите Enter для вывода транзакции")
    print(next(usd_transactions))
print("Все транзакции были выведены на экран")


# Тест функции transaction_descriptions
descriptions = transaction_descriptions(transactions)
for i in range(5):
    next_transact = input("Введите Enter для вывода информации по транзакции")
    print(next(descriptions))


# Тест функции card_number_generator
start_input = int(input("Введите начальный диапазон номеров карт: "))
end_input = int(input("Введите конечный диапазон номеров карт: "))
print("===========================")
for card_number in card_number_generator(start_input, end_input):
    print(card_number)

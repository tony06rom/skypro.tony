from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions


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
    next_transact = input(f"Введите Enter для вывода транзакции или введите 'quit' для выхода")
    print(next(usd_transactions))
print("Все транзакции были выведены на экран")
![SkyPro_image](/data/images/for_readme_file/SkyPro.png)
![Python_image](/data/images/for_readme_file/Python.png)
![Git_image](/data/images/for_readme_file/Git.png)
![GitHub_image](/data/images/for_readme_file/GitHub.png)

# Первые шаги в Python с использованием GitHub
## Здесь будет проводиться разработка (обучение) приложения
### homework_10_1

Приложение на данный момент содержит:
- модули (masks, widget, processing)
- в каждом модуле имеются свои функции
- gitignore настроен на работу с PyCharm
- подключены линтеры
- локальный Git связан с репозиторием на GitHub
- 
===============================================================================================

### Логика готовой программы

1. Программа дает на выбор пользователю три варианта: работа с json, csv и excel файлами транзакций
2. Следующим шагом пользователю предоставляется выбор возможных файлов
3. Если файл содержит корректные данные, то пользователю предлагается выбрать статус транзакции (отфильтровать)
4. Следующий запрос: сортировка по дате транзакции (по возрастанию\убыванию)
5. Последний шаг: сортировка по слову в описании транзакции

В итоге получается список транзакций с основной информацией: дата, тип операции, счета\карты и сумма операции



===============================================================================================

### Инструкции для модулей:

1. Модуль _**masks**_
   - Доступные функции:
     - get_mask_card_number
     - get_mask_account 

     _Пример импорта:_
       ```
     from src.masks import get_mask_card_number
       ```

     <details>
     <summary>Пример работы:</summary>
      
     [![Example_masks][1]][1]
   
      [1]: /data/images/for_readme_file/Example_masks.png
      </details>
   
   
2. Модуль _**widget**_
    - Доступные функции:
      - mask_account_card
      - get_date 
      
      _Пример импорта:_
        ```
      from src.widget import mask_account_card
        ```

       <details>
       <summary>Пример работы:</summary>
      
       [![Example_widget][2]][2]
   
       [2]: /data/images/for_readme_file/Example_widget.png
       </details>

   
3. Модуль _**processing**_
    - Доступные функции:
      - filter_by_state
      - sort_by_date
      
      _Пример импорта:_
        ```
      from src.processing import get_mask_card_number
      ```

       <details>
       <summary>Пример работы:</summary>
      
       [![Example_processing][3]][3]
   
       [3]: /data/images/for_readme_file/Example_processing.png
       </details>
    
4. Модуль _**generators**_
    - Доступные функции:
      - filter_by_currency
      - transaction_descriptions
      - card_number_generator
      
      _Пример импорта:_
        ```
      from src.generators import filter_by_currency
      ```

       <details>
       <summary>Пример работы:</summary>
      
       [![Example_processing][4]][4]
   
       [4]: /data/images/for_readme_file/Example_generators.png
       </details>
    
5. Модуль _**decorators**_
    - Доступные функции:
      - decor_log
      
      _Пример импорта:_
        ```
      from src.decorators import decor_log as decor
      ```

       <details>
       <summary>Пример работы:</summary>
      
       [![Example_decorators][5]][5]
   
       [5]: /data/images/for_readme_file/Example_decorators.png
       </details>
    
6. Модуль _**utils**_
    - Доступные функции:
      - read_json_file
      - summ_transact_rub
      
      _Пример импорта:_
        ```
      from src.utils import read_json_file
      ```
       Пример работы будет позднее. Исчерпан лимит использования API
    
7. Модуль _**external_api**_
    - Доступные функции:
      - convert_amount
      
      _Пример импорта:_
        ```
      from src.external_api import convert_amount
      ```
      Пример работы будет позднее. Исчерпан лимит использования API

8. Модуль _**csv_pandas**_
    - Доступные функции:
      - csv_worker
      - excel_worker
      
      _Пример импорта:_
        ```
      from src.csv_pandas import csv_worker
      ```

       <details>
       <summary>Пример работы:</summary>
      
       [![Example_csv_pandas][8]][8]
   
       [8]: /data/images/for_readme_file/Example_csv_pandas.png
       </details>
   
9. Модуль _**re_collections**_
    - Доступные функции:
      - filter_by_description
      
      _Пример импорта:_
        ```
      from src.re_collections import filter_by_description
      ```

      **Назначение модуля:**
         Поиск списка словарей по значению указанного ключа

      <details>
      <summary>Пример работы:</summary>
      - будет позже. Сейчас можно ознакомиться в последнем пункте работы всей программы через файл main.py в корне проекта
      </details>   

10. Модуль _**transact_counter**_
    - Доступные функции:
      - transact_counter
      
      _Пример импорта:_
        ```
      from src.transact_counter import transact_counter
      ```

      **Назначение модуля:**
         Считает количество банковских операций по категории

      <details>
      <summary>Пример работы:</summary>
      - будет позже
      </details>   
   
   
Все тесты функций можно выполнять из директории [moduls_test](/moduls_test)

===============================================================================================
## Pytest

Реализовано тестирование функций при помощи pytest.
Отчет реализован в импорте в [html](/htmlcov)
На данный момент покрыто тестами 90% функций проекта (скриншоты отчёта):

   <details>
   <summary>Проверка по файлам:</summary>
  
   [![Example_processing][5]][5]

   [5]: /data/images/for_readme_file/Pytest_files.png
   </details>

   <details>
   <summary>Проверка по функциям:</summary>
  
   [![Example_processing][6]][6]

   [6]: /data/images/for_readme_file/Pytest_functions.png
   </details>

   <details>
   <summary>Проверка по классам:</summary>
  
   [![Example_processing][7]][7]

   [7]: /data/images/for_readme_file/Pytest_classes.png
   </details>


===============================================================================================

## logging

На данный момент логирование реализовано для модулей **masks** и **utils**

### Директория логов: ```../logs```

### Доступные уровни логирования:
- critical
- error
- warning
- info
- debug

### Доступные форматы логирования:
* __%(asctime)s__ — дата и время события логирования
* __%(name)s__ — имя логера
* __%(levelname)s__ — уровень логирования
* __%(message)s__ — текст сообщения
* __%(filename)s__ — имя файла, в котором произошло событие
* __%(funcName)s__ — имя функции, в которой произошло событие
* __%(lineno)d__ — номер строки, в которой произошло событие
* __%(process)d__ — ID процесса
* __%(thread)d__ — ID потока

### Используемый формат логов:
```%(asctime)s | %(name)s | %(levelname)s | %(funcName)s: %(message)s```

   <details>
   <summary>Пример лога (utils):</summary>
  
   [![Example_logging][8]][8]

   [8]: /data/images/for_readme_file/Example_logging.png
   </details>


===============================================================================================

## Проблемы тестирования

1. Функция **summ_transact_rub** не протестирована
2. Функция **convert_amount** в модуле **external_api** не протестирована на возврат нулевого значения
3. Функции в модуле **masks** не протестированы на циклический запуск функции
4. Функция **mask_account_card** в модуле **widget** не протестированы на циклический запуск функции
5. Модуль **src.linking_functions_main.py** не протестирован, так как является не обязательным и вспомогательным для логики в main
6. Функция **summ_transact_rub** в модуле **utils** не протестирована, так как имеет сложную логику

## Полезные команды тестирования

Формирование отчёта в html:
```pytest --cov=src --cov-report=html```
Отчёт в консоли:
```run pytest --cov```
Проверка тестовых файлов:
```pytest -cov```

===============================================================================================

## Примечания по проекту
1. Пришлось установить библиотеки для mypy:
    ```mypy --install-types```


===============================================================================================

## Проблемы проекта

На данный момент ***mypy*** не выдает ошибки


===============================================================================================

Этот проект выполняется совместно с [SkyPro](https://sky.pro/)
####  Автор проекта: **Romanenko Anton**

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
      
Все тесты функций можно выполнять из директории [tests](/tests)

===============================================================================================
## Pytest

Реализовано тестирование функций при помощи pytest.
Отчет реализован в импорте в [html](/htmlcov) (```pytest --cov=src --cov-report=html```)
На данный момент покрыто тестами 100% функций проекта (скриншоты отчёта):

   <details>
   <summary>Проверка по файлам:</summary>
  
   [![Example_processing][4]][4]

   [4]: /data/images/for_readme_file/Pytest_files.png
   </details>

   <details>
   <summary>Проверка по функциям:</summary>
  
   [![Example_processing][4]][4]

   [4]: /data/images/for_readme_file/Pytest_functions.png
   </details>

   <details>
   <summary>Проверка по классам:</summary>
  
   [![Example_processing][4]][4]

   [4]: /data/images/for_readme_file/Pytest_classes.png
   </details>

===============================================================================================

## Проблемы проекта

На данный момент ***mypy*** выдает 2 ошибки

> src\widget.py:24: error: Missing return statement  [return]
 
> src\widget.py:31: error: Incompatible types in assignment (expression has type "list[str]", variable has type "str")  [assignment]

===============================================================================================

Этот проект выполняется совместно с [SkyPro](https://sky.pro/)
####  Автор проекта: **Romanenko Anton**

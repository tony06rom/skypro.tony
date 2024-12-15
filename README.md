![SkyPro_image](/data/images/SkyPro.png)
![Python_image](/data/images/Python.png)
![Git_image](/data/images/Git.png)
![GitHub_image](/data/images/GitHub.png)

# Первые шаги в Python с использованием GitHub
## Здесь будет проводиться разработка (обучение) приложения
### homework_10_1

Приложение на данный момент содержит:
- модули (masks, widget, processing)
- в каждом модуле имеются свои функции
- gitignore настроен на работу с PyCharm
- подключены линтеры
- локальный Git связан с репозиторием на GitHub

### Инструкции для модулей:

1. Модуль _**masks**_
   - Доступные функции:
     - get_mask_card_number
     - get_mask_account 

     _Пример импорта:_
       ```
     from src.masks import *****
       ```

     <details>
     <summary>Пример работы:</summary>
      
     [![Example_masks][1]][1]
   
      [1]: /data/images/Example_masks.png
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
      
       [![Example_widget][1]][1]
   
       [1]: /data/images/Example_widget.png
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
      
       [![Example_processing][1]][1]
   
       [1]: /data/images/Example_processing.png
       </details>
      
Все тесты функций можно выполнять из директории [tests](/tests)

Этот проект выполняется совместно с [SkyPro](https://sky.pro/)
####  Автор проекта: **Romanenko Anton**

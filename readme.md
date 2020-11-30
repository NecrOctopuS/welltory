# Проверка эвентов на соответствие схемам

Скрипт проверяет эвенты в папке `task_folder/event` на соответствие схемам из папки `task_folder/schema`.

## Запуск

Для запуска сайта у вас уже должен быть установлен Python 3.

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Запускаем скрипт: 
```
python3 welltory.py
```

Будет создан файл `app.log` с результатами проверок.

## Результат работы скрипта
```
10996|WARNING|task_folder/event\29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json is not valid json.
10996|WARNING|task_folder/event\a95d845c-8d9e-4e07-8948-275167643a40.json is not valid json.
10996|ERROR|Event task_folder/event\1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json not validated by task_folder/schema\cmarker_created.schema because 'cmarkers' is a required property.
10996|ERROR|Event task_folder/event\297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json not validated by task_folder/schema\cmarker_created.schema because 'cmarkers' is a required property.
10996|ERROR|Event task_folder/event\2e8ffd3c-dbda-42df-9901-b7a30869511a.json not validated by task_folder/schema\cmarker_created.schema because 'cmarkers' is a required property.
10996|ERROR|Event task_folder/event\3ade063d-d1b9-453f-85b4-dda7bfda4711.json not validated by task_folder/schema\cmarker_created.schema because 'cmarkers' is a required property.
10996|ERROR|Event task_folder/event\3b4088ef-7521-4114-ac56-57c68632d431.json not validated by task_folder/schema\cmarker_created.schema because 'cmarkers' is a required property.
10996|ERROR|Event task_folder/event\6b1984e5-4092-4279-9dce-bdaa831c7932.json not validated by task_folder/schema\cmarker_created.schema because 'cmarkers' is a required property.
10996|ERROR|Event task_folder/event\ba25151c-914f-4f47-909a-7a65a6339f34.json not validated by task_folder/schema\cmarker_created.schema because 'cmarkers' is a required property.
10996|ERROR|Event task_folder/event\bb998113-bc02-4cd1-9410-d9ae94f53eb0.json not validated by task_folder/schema\cmarker_created.schema because 'cmarkers' is a required property.
10996|ERROR|Event task_folder/event\c72d21cf-1152-4d8e-b649-e198149d5bbb.json not validated by task_folder/schema\cmarker_created.schema because 'cmarkers' is a required property.
10996|ERROR|Event task_folder/event\cc07e442-7986-4714-8fc2-ac2256690a90.json not validated by task_folder/schema\cmarker_created.schema because 'cmarkers' is a required property.
10996|ERROR|Event task_folder/event\e2d760c3-7e10-4464-ab22-7fda6b5e2562.json not validated by task_folder/schema\cmarker_created.schema because 'cmarkers' is a required property.
10996|ERROR|Event task_folder/event\f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json not validated by task_folder/schema\cmarker_created.schema because 'cmarkers' is a required property.
10996|ERROR|Event task_folder/event\fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json not validated by task_folder/schema\cmarker_created.schema because 'cmarkers' is a required property.
10996|ERROR|Event task_folder/event\ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json not validated by task_folder/schema\cmarker_created.schema because 'cmarkers' is a required property.
10996|ERROR|Event task_folder/event\1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json not validated by task_folder/schema\label_selected.schema because 'id' is a required property.
10996|ERROR|Event task_folder/event\297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json not validated by task_folder/schema\label_selected.schema because 'labels' is a required property.
10996|ERROR|Event task_folder/event\2e8ffd3c-dbda-42df-9901-b7a30869511a.json not validated by task_folder/schema\label_selected.schema because 'labels' is a required property.
10996|ERROR|Event task_folder/event\3ade063d-d1b9-453f-85b4-dda7bfda4711.json not validated by task_folder/schema\label_selected.schema because 'labels' is a required property.
10996|ERROR|Event task_folder/event\3b4088ef-7521-4114-ac56-57c68632d431.json not validated by task_folder/schema\label_selected.schema because 'labels' is a required property.
10996|ERROR|Event task_folder/event\6b1984e5-4092-4279-9dce-bdaa831c7932.json not validated by task_folder/schema\label_selected.schema because 'labels' is a required property.
10996|ERROR|Event task_folder/event\ba25151c-914f-4f47-909a-7a65a6339f34.json not validated by task_folder/schema\label_selected.schema because 'id' is a required property.
10996|ERROR|Event task_folder/event\bb998113-bc02-4cd1-9410-d9ae94f53eb0.json not validated by task_folder/schema\label_selected.schema because 'labels' is a required property.
10996|ERROR|Event task_folder/event\c72d21cf-1152-4d8e-b649-e198149d5bbb.json not validated by task_folder/schema\label_selected.schema because 'labels' is a required property.
10996|ERROR|Event task_folder/event\cc07e442-7986-4714-8fc2-ac2256690a90.json not validated by task_folder/schema\label_selected.schema because 'id' is a required property.
10996|ERROR|Event task_folder/event\e2d760c3-7e10-4464-ab22-7fda6b5e2562.json not validated by task_folder/schema\label_selected.schema because 'labels' is a required property.
10996|ERROR|Event task_folder/event\f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json not validated by task_folder/schema\label_selected.schema because 'labels' is a required property.
10996|ERROR|Event task_folder/event\fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json not validated by task_folder/schema\label_selected.schema because 'labels' is a required property.
10996|ERROR|Event task_folder/event\ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json not validated by task_folder/schema\label_selected.schema because 'labels' is a required property.
10996|ERROR|Event task_folder/event\1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json not validated by task_folder/schema\sleep_created.schema because 'source' is a required property.
10996|ERROR|Event task_folder/event\297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json not validated by task_folder/schema\sleep_created.schema because 'source' is a required property.
10996|ERROR|Event task_folder/event\2e8ffd3c-dbda-42df-9901-b7a30869511a.json not validated by task_folder/schema\sleep_created.schema because 'source' is a required property.
10996|ERROR|Event task_folder/event\3ade063d-d1b9-453f-85b4-dda7bfda4711.json not validated by task_folder/schema\sleep_created.schema because 'source' is a required property.
10996|ERROR|Event task_folder/event\3b4088ef-7521-4114-ac56-57c68632d431.json not validated by task_folder/schema\sleep_created.schema because 'source' is a required property.
10996|ERROR|Event task_folder/event\6b1984e5-4092-4279-9dce-bdaa831c7932.json not validated by task_folder/schema\sleep_created.schema because 'source' is a required property.
10996|ERROR|Event task_folder/event\ba25151c-914f-4f47-909a-7a65a6339f34.json not validated by task_folder/schema\sleep_created.schema because 'source' is a required property.
10996|ERROR|Event task_folder/event\bb998113-bc02-4cd1-9410-d9ae94f53eb0.json not validated by task_folder/schema\sleep_created.schema because 'source' is a required property.
10996|ERROR|Event task_folder/event\c72d21cf-1152-4d8e-b649-e198149d5bbb.json not validated by task_folder/schema\sleep_created.schema because 'source' is a required property.
10996|ERROR|Event task_folder/event\cc07e442-7986-4714-8fc2-ac2256690a90.json not validated by task_folder/schema\sleep_created.schema because 'source' is a required property.
10996|ERROR|Event task_folder/event\e2d760c3-7e10-4464-ab22-7fda6b5e2562.json not validated by task_folder/schema\sleep_created.schema because 'source' is a required property.
10996|ERROR|Event task_folder/event\f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json not validated by task_folder/schema\sleep_created.schema because 'source' is a required property.
10996|ERROR|Event task_folder/event\fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json not validated by task_folder/schema\sleep_created.schema because 'source' is a required property.
10996|ERROR|Event task_folder/event\ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json not validated by task_folder/schema\sleep_created.schema because 'source' is a required property.
10996|ERROR|Event task_folder/event\1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json not validated by task_folder/schema\workout_created.schema because 'activity_name' is a required property.
10996|ERROR|Event task_folder/event\297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json not validated by task_folder/schema\workout_created.schema because 'activity_name' is a required property.
10996|ERROR|Event task_folder/event\2e8ffd3c-dbda-42df-9901-b7a30869511a.json not validated by task_folder/schema\workout_created.schema because 'activity_name' is a required property.
10996|ERROR|Event task_folder/event\3ade063d-d1b9-453f-85b4-dda7bfda4711.json not validated by task_folder/schema\workout_created.schema because 'activity_name' is a required property.
10996|ERROR|Event task_folder/event\3b4088ef-7521-4114-ac56-57c68632d431.json not validated by task_folder/schema\workout_created.schema because 'activity_name' is a required property.
10996|ERROR|Event task_folder/event\6b1984e5-4092-4279-9dce-bdaa831c7932.json not validated by task_folder/schema\workout_created.schema because 'activity_name' is a required property.
10996|ERROR|Event task_folder/event\ba25151c-914f-4f47-909a-7a65a6339f34.json not validated by task_folder/schema\workout_created.schema because 'activity_name' is a required property.
10996|ERROR|Event task_folder/event\bb998113-bc02-4cd1-9410-d9ae94f53eb0.json not validated by task_folder/schema\workout_created.schema because 'activity_name' is a required property.
10996|ERROR|Event task_folder/event\c72d21cf-1152-4d8e-b649-e198149d5bbb.json not validated by task_folder/schema\workout_created.schema because 'activity_name' is a required property.
10996|ERROR|Event task_folder/event\cc07e442-7986-4714-8fc2-ac2256690a90.json not validated by task_folder/schema\workout_created.schema because 'activity_name' is a required property.
10996|ERROR|Event task_folder/event\e2d760c3-7e10-4464-ab22-7fda6b5e2562.json not validated by task_folder/schema\workout_created.schema because 'activity_name' is a required property.
10996|ERROR|Event task_folder/event\f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json not validated by task_folder/schema\workout_created.schema because 'activity_name' is a required property.
10996|ERROR|Event task_folder/event\fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json not validated by task_folder/schema\workout_created.schema because 'activity_name' is a required property.
10996|ERROR|Event task_folder/event\ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json not validated by task_folder/schema\workout_created.schema because 'activity_name' is a required property.
```

## Цели проекта

Код написан в качестве тестового задания для Welltory.
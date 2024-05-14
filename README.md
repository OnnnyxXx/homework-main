# Мини Таск менеджер.

### Docker
- https://docs.docker.com/desktop/install/linux-install/

- docker build . -t fastapp_app:latest
- Waiting
- docker run -p 8000:8000 fastapp_app
- http://127.0.0.1:8000/docs
- docker stop fastapp_app 

### requirements:

- poetry
- fastapi
- uvicorn

## Для проверки корректности работы рекомендую запустить тесты.

## Суть задания:
```
У нас есть 2 маршрута. Создать задачу/прочитать все задачи. 

- Функционал прочитать есть, но работает с ошибкой. (Надо исправить)
- Фунционал создания с валидицией данных нужно дописать. Что будете использовать для валидации
не принципиально.
- Для удобство обернуть в докер.
- Написать как это запустить...
```

## Будет плюсом:
```
- Добавить doc string.
- Добавить функционал для хранения данных в другом хранилище. (SQL, NoSQL и пр..)
- Написать в док к JSONStorage, почему это плохое решение.
```

### Сущность Task:
```
 id: int
 title: string
 completed: bool
 created_at: datetime
 updated_at: datetime
```

# Документация на мой API
На сервере хранятся заказы некоторй компании, они имеют поля:
1) Id - id заказа в системе
2) Product - название товара
3) Price - цена
4) Quantity - количество товара
5) Client - имя клиента, оставившего заказ

все заказы хранятся в списке словарей. По умолчанию в списке один шаблонный заказ:
   {
        'id': 1,
        'product': 'Pencils',
        'price': 100,
        'quantity': 2,
        'client': 'John'
    }

API сервера реализует 8 end-pointов
1) [GET] /api/orders - получить все заказы
2) [POST] /api/orders - добавить новый заказ, все поля заказа, кроме id передаются JSONом в параметры запроса
3) [GET] /api/orders/<int:order_id> - получить заказ по id
4) [PATCH] /api/orders/<int:order_id> - частично изменить заказ по id
5) [PUT] /api/orders/<int:order_id> - полностью изменить заказ по id
6) [DELETE] /api/orders/<int:order_id> - удалить заказ по id
7) [GET] /api/orders/reset_to_default - сбросить список заказов до состояния по умолчанию
8) [DELETE] /api/orders - удалить все заказы

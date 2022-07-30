from configs.init_config import app, db
from utils import DBTools, JSONTools
from app.users.view import bp_users
from app.offers.view import bp_offers
from app.orders.view import bp_orders


app.register_blueprint(bp_users, url_prefix="/users")
app.register_blueprint(bp_offers, url_prefix="/offers")
app.register_blueprint(bp_orders, url_prefix="/orders")

db_tools = DBTools()
json_tools = JSONTools()

# Добавляем таблицы в базу
db.drop_all()
db.create_all()

# Заполняем таблицы в базе
# with db.session.begin():
user_data = json_tools.load(app.config.get("USERS_DATA"))
orders_data = json_tools.load(app.config.get("ORDERS_DATA"))
offers_data = json_tools.load(app.config.get("OFFERS_DATA"))
db_tools.insert_users_data(user_data)
db_tools.insert_orders_data(orders_data)
db_tools.insert_offers_data(offers_data)


if __name__ == '__main__':
    app.run()

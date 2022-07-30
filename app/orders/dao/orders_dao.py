from utils import DBTools

db_tools = DBTools()


class OrdersDAO:
    def get_all(self):
        return db_tools.extract_orders_data()

    def get_by_id(self, oid: int):
        orders: list[dict] = db_tools.extract_orders_data()
        return [order for order in orders if order.get("id") == oid]

    def add(self, data: list[dict]) -> bool:
        return db_tools.insert_orders_data(data)

    def update(self, data: dict, oid: int) -> bool:
        return db_tools.update_order_data(data, oid)

    def delete(self, oid: int) -> bool:
        return db_tools.delete_order(oid)

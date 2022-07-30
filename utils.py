import json
from json import JSONDecodeError

from configs.init_config import db
from models.models import User, Order, Offer


class DBTools:

    def insert_users_data(self, data: list[dict]) -> bool:
        try:
            with db.session.begin():
                for user_data in data:
                    db.session.add(
                        User(
                            id=user_data.get("id"),
                            first_name=user_data.get("first_name"),
                            last_name=user_data.get("last_name"),
                            age=user_data.get("age"),
                            email=user_data.get("email"),
                            role=user_data.get("role"),
                            phone=user_data.get("phone")
                        )
                    )
                db.session.commit()
        except Exception:
            return False
        else:
            return True

    def insert_orders_data(self, data: list[dict]) -> bool:
        try:
            with db.session.begin():
                for order_data in data:
                    db.session.add(
                        Order(
                            id=order_data.get("id"),
                            name=order_data.get("name"),
                            description=order_data.get("description"),
                            start_date=order_data.get("start_date"),
                            end_date=order_data.get("end_date"),
                            address=order_data.get("address"),
                            price=order_data.get("price"),
                            customer_id=order_data.get("customer_id"),
                            executor_id=order_data.get("executor_id"),
                        )
                    )
                db.session.commit()
        except Exception:
            return False
        else:
            return True

    def insert_offers_data(self, data: list[dict]) -> bool:
        try:
            with db.session.begin():
                for offer_data in data:
                    db.session.add(
                        Offer(
                            id=offer_data.get("id"),
                            order_id=offer_data.get("order_id"),
                            executor_id=offer_data.get("executor_id"),
                        )
                    )
                db.session.commit()
        except Exception:
            return False
        else:
            return True

    def extract_users_data(self) -> list[dict]:
        users = db.session.query(User).all()
        return [user.get_data() for user in users]

    def extract_orders_data(self) -> list[dict]:
        orders = db.session.query(Order).all()
        return [order.get_data() for order in orders]

    def extract_offers_data(self) -> list[dict]:
        offers = db.session.query(Offer).all()
        return [offer.get_data() for offer in offers]

    def update_user_data(self, new_data: dict, uid: int) -> bool:
        try:
            with db.session.begin():
                user = db.session.query(User).get(uid)
                user.id = uid
                user.first_name = new_data.get("first_name")
                user.last_name = new_data.get("last_name")
                user.age = new_data.get("age")
                user.email = new_data.get("email")
                user.role = new_data.get("role")
                user.phone = new_data.get("phone")
                db.session.add(user)
                db.session.commit()
        except Exception:
            return False
        else:
            return True

    def update_order_data(self, new_data: dict, oid: int) -> bool:
        try:
            with db.session.begin():
                order = db.session.query(Order).get(oid)
                order.id = oid
                order.name = new_data.get("name")
                order.description = new_data.get("description")
                order.start_date = new_data.get("start_date")
                order.end_date = new_data.get("end_date")
                order.address = new_data.get("address")
                order.price = new_data.get("price")
                order.customer_id = new_data.get("customer_id")
                order.executor_id = new_data.get("executor_id")
                db.session.add(order)
                db.session.commit()
        except Exception:
            return False
        else:
            return True

    def update_offer_data(self, new_data: dict, oid: int) -> bool:
        try:
            with db.session.begin():
                offer = db.session.query(Offer).get(oid)
                offer.id = oid
                offer.order_id = new_data.get("order_id")
                offer.executor_id = new_data.get("executor_id")
                db.session.add(offer)
                db.session.commit()
        except Exception:
            return False
        else:
            return True

    def delete_user(self, uid: int) -> bool:
        try:
            with db.session.begin():
                db.session.query(User).filter(User.id == uid).delete()
        except Exception:
            return False
        else:
            return True

    def delete_order(self, oid: int) -> bool:
        try:
            with db.session.begin():
                db.session.query(Order).filter(Order.id == oid).delete()
        except Exception:
            return False
        else:
            return True

    def delete_offer(self, oid: int) -> bool:
        try:
            with db.session.begin():
                db.session.query(Offer).filter(Offer.id == oid).delete()
        except Exception:
            return False
        else:
            return True

class JSONTools:

    def load(self, path: str) -> list[dict] | None:
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except JSONDecodeError:
                return None

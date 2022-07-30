from utils import DBTools

db_tools = DBTools()


class UsersDAO:
    def get_all(self) -> list[dict]:
        return db_tools.extract_users_data()

    def get_by_id(self, uid: int) -> list[dict]:
        users: list[dict] = db_tools.extract_users_data()
        return [user for user in users if user.get("id") == uid]

    def add(self, data: list[dict]) -> bool:
        return db_tools.insert_users_data(data)

    def update(self, data: dict, uid: int) -> bool:
        return db_tools.update_user_data(data, uid)

    def delete(self, uid: int) -> bool:
        return db_tools.delete_user(uid)

from utils import DBTools

db_tools = DBTools()


class OffersDAO:
    def get_all(self):
        return db_tools.extract_offers_data()

    def get_by_id(self, oid: int):
        offers: list[dict] = db_tools.extract_offers_data()
        return [offer for offer in offers if offer.get("id") == oid]

    def add(self, data: list[dict]) -> bool:
        return db_tools.insert_offers_data(data)

    def update(self, data: dict, oid: int) -> bool:
        return db_tools.update_offer_data(data, oid)

    def delete(self, oid: int) -> bool:
        return db_tools.delete_offer(oid)

from models.abstract import AbstractModel, ElementDoesNotExist

class Mesa(AbstractModel):
    COLLECTION = "mesas"

    number = None
    users = []

    def __init__(
            self,
            number,
            users,
            _id=None
    ):
        super().__init__(_id)
        self.number = number
        self.users = users

    def prepare_to_save(self):
        return {
            "number": self.number,
            "users": self.users
        }

    def to_json(self):
        return self.__dict__

    @staticmethod
    def create(content):
        return Mesa(
            number=content["number"],
            users=content["users"],
            _id=str(content["_id"]) if content.get("_id") else None
        )

class MesaDoesNotExist(ElementDoesNotExist):
    pass
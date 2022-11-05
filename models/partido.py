from models.abstract import AbstractModel, ElementDoesNotExist

class Partido(AbstractModel):
    COLLECTION = "parties"

    name = None

    def __init__(
            self,
            nombre,
            lema,
            _id=None
    ):
        super().__init__(_id)
        self.nombre = nombre
        self.lema = lema

    def prepare_to_save(self):
        return {
            "nombre": self.nombre,
            "lema": self.lema
        }

    def to_json(self):
        return self.__dict__

    @staticmethod
    def create(content):
        return Partido(
            nombre=content["nombre"],
            lema=content["lema"],
            _id=str(content["_id"]) if content.get("_id") else None
        )

class PartyDoesNotExist(ElementDoesNotExist):
    pass
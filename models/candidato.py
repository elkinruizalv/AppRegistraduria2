from models.abstract import AbstractModel, ElementDoesNotExist
from models.partido import Partido
from bson import DBRef, ObjectId


class Candidato(AbstractModel):
    COLLECTION = "candidatos"

    nombre = None
    apellido = None
    cedula = None
    resolucion = None
    partido: Partido = None

    def __init__(
            self,
            nombre,
            apellido,
            cedula,
            resolucion,
            partido = None,
            _id = None
    ):
        super().__init__(_id)
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.resolucion= resolucion
        self.partido = partido

    def prepare_to_save(self):
        partido_db_ref = None
        if self.partido:
            partido_db_ref = DBRef(
                id=ObjectId(self.partido["_id"]),
                collection=Partido.COLLECTION
            )
        return {
            "nombre": self.nombre,
            "apellido":self.apellido,
            "cedula": self.cedula,
            "resolucion":self.resolucion,
            "partido": partido_db_ref
        }

    def to_json(self):
        partido = None
        if self.partido:
            partido = self.partido.to_json()
        return {
            "_id": self._id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "cedula": self.cedula,
            "resolucion":self.resolucion,
            "partido": partido
        }

    @staticmethod
    def create(content):
        partido = None
        if (content.get("partido")):
            partido = Partido.create(content.get("partido"))
        return Candidato(
            nombre=content["nombre"],
            apellido=content["apellido"],
            cedula=content["cedula"],
            resolucion=content["resolucion"],
            partido=partido,
            _id=str(content["_id"]) if content.get("_id") else None
        )


class CandidatoDoesNotExist(ElementDoesNotExist):
    pass
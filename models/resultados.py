from models.abstract import AbstractModel, ElementDoesNotExist

from bson import DBRef, ObjectId
from models.mesa import Mesa
from models.candidato import Candidato


class Resultados(AbstractModel):
    COLLECTION = "Resultados"

    user_id = None
    mesa: Mesa = None
    candidato: Candidato = None

    def __init__(
            self,
            user_id,
            mesa = None,
            candidato = None,
            _id = None
    ):
        super().__init__(_id)
        self.user_id = user_id
        self.mesa = mesa
        self.candidato = candidato

    def prepare_to_save(self):
        return {
            "mesa": DBRef(
                id=ObjectId(self.mesa["_id"]),
                collection=Mesa.COLLECTION
            ),
            "candidato": DBRef(
                id=ObjectId(self.candidato["_id"]),
                collection=Candidato.COLLECTION
            ),
            "user_id": self.user_id
        }

    def to_json(self):
        mesa = None
        candidato = None
        if self.mesa:
            mesa = self.mesa.to_json()
        if self.candidate:
            candidato = self.candidato.to_json()
        return {
            "_id": self._id,
            "user_id": self.user_id,
            "candidato": candidato,
            "mesa": mesa
        }

    @staticmethod
    def create(content):
        assert content.get("candidato")
        assert content.get("mesa")
        mesa = Mesa.create(content.get('mesa'))
        candidato = Candidato.create(content.get('candidato'))
        return Resultados(
            user_id=content.get("user_id"),
            candidato=candidato,
            mesa=mesa,
            _id=str(content["_id"]) if content.get("_id") else None
        )


class ResultadosDoesNotExist(ElementDoesNotExist):
    pass
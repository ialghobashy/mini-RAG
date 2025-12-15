from .BaseDataModel import BaseDataModel
from .db_schemes import Project
from .enums.DatabaseEnum import DatabaseEnum

class ProjectModel(BaseDataModel):
    def __init__(self, db_client:object):
        super().__init__(db_client)
        self.collection = self.db_client[DatabaseEnum.COLLECTION_PROJECT_NAME.value]

    

from elasticsearch import Elasticsearch
from abc import abstractmethod, ABCMeta
from typing import Dict, List
from pydantic import BaseModel


class ElasticEntityRepositoryBase(object):
    __metaclass__ = ABCMeta

    # -----------------------------------------------------
    # CONSTRUCTOR METHOD
    # -----------------------------------------------------
    def __init__(
            self,
            index: str,
            elasticsearch_client: Elasticsearch
    ):
        self.index = index
        self.elasticsearch_client: Elasticsearch = \
            elasticsearch_client

    # -----------------------------------------------------
    # QUERY
    # -----------------------------------------------------
    def search(self, query: dict) -> List[Dict]:
        q = {
            'size': 10000,
            'query': query
        }
        result = self.elasticsearch_client.search(
            index=self.index,
            body=q,
            scroll='1m'
        )
        matches: List[Dict] = []
        if 'hits' in result and 'hits' in result['hits']:
            for match in result['hits']['hits']:
                matches.append(match['_source'])
        return matches

    # -----------------------------------------------------
    # QUERY
    # -----------------------------------------------------
    def get(self, entity_id: str) -> Dict or None:
        result = self.elasticsearch_client.get(
            index=self.index,
            id=entity_id
        )
        if result is not None and '_source' in result:
            return result['_source']
        return None

    # -----------------------------------------------------
    # CREATE
    # -----------------------------------------------------
    def create(self, entity: BaseModel, document_id: Dict):
        pass
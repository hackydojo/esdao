from abc import ABCMeta, abstractmethod
from typing import List


# ---------------------------------------------------------
# CLASS ELASTICSEARCH QUERY ELEMENT
#  --------------------------------------------------------
class DSLQueryElement(object):
    __metaclass__ = ABCMeta

    def __init__(self, field_name: str, value: str):
        self._field_name = field_name
        self._value = value

    @abstractmethod
    def dict(self):
        pass

    @property
    def field(self) -> str:
        return self._field_name

    @property
    def value(self) -> str:
        return self._value


# ---------------------------------------------------------
# CLASS MATCH
# ---------------------------------------------------------
class Match(DSLQueryElement):

    def __init__(self, field_name: str, value: str):
        super().__init__(field_name, value)

    def dict(self):
        return {
            "match": {
                self.field: self.value
            }
        }


# ---------------------------------------------------------
# CLASS ELASTICSEARCH FIELD QUERY
# ---------------------------------------------------------
class ElasticSearchFieldQuery(object):

    def __init__(self):
        self._should: List[dict] = []
        self._must: List[dict] = []
        self._should_not: List[dict] = []
        self._must_not: List[dict] = []
        self.query: dict = {
            "size": 10000,
            "query": {
                "bool": {}
            }
        }

    def set_minimum_number_should_match(self, number: int):
        self.query['query']['bool']['minimum_number_should_match'] = number

    def set_size(self, size: int):
        self.query['size'] = size
        return self

    def must(self, query_element: DSLQueryElement):
        self._must.append(query_element.dict())
        return self

    def should(self, query_element: DSLQueryElement):
        self._should.append(query_element.dict())
        return self

    def should_not(self, query_element: DSLQueryElement):
        self._should_not.append(query_element.dict())
        return self

    def must_not(self, query_element: DSLQueryElement):
        self._must_not.append(query_element.dict())
        return self

    def _add_if_available(self, condition: str, query_elements: list):
        if len(query_elements) > 0:
            self.query['query']['bool'][condition] = query_elements

    def dict(self):
        self._add_if_available('should', self._should)
        self._add_if_available('should_not', self._should_not)
        self._add_if_available('must', self._must)
        self._add_if_available('must_not', self._must_not)
        return self.query

    def clear(self):
        self.query['query']['bool'] = {}


# ---------------------------------------------------------
# CLASS DOCUMENT FIELD QUERY ADAPTER
# ---------------------------------------------------------
class DocumentFieldQueryAdapter(object):


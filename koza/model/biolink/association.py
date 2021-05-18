"""
Biolink Model Dataclasses + Pydantic validators

Longer term generate this from Biolink model yaml
https://github.com/biolink/biolink-model/blob/master/biolink-model.yaml

"""

from dataclasses import field
from typing import ClassVar, List, Union

from pydantic.dataclasses import dataclass

from koza.validator.model_validator import convert_object_to_scalar, convert_objects_to_scalars

from ..config.pydantic_config import PydanticConfig
from ..curie import Curie
from .named_thing import Entity, Publication


@dataclass(config=PydanticConfig)
class Association(Entity):
    """
    A typed association between two entities, supported by evidence
    """

    _category: ClassVar[str] = 'Association'

    subject: Union[Entity, Curie] = None
    predicate: Union[Entity, Curie] = None
    object: Union[Entity, Curie] = None
    relation: str = None
    negated: bool = False
    qualifiers: List[Curie] = field(default_factory=list)
    publications: List[Union[Publication, Curie]] = field(default_factory=list)
    type: Curie = 'rdf:Statement'

    # converters
    _subject_to_scalar = convert_object_to_scalar('subject')
    _predicate_to_scalar = convert_object_to_scalar('predicate')
    _object_to_scalar = convert_object_to_scalar('object')
    _publication_to_scalar = convert_objects_to_scalars('publications')


@dataclass(config=PydanticConfig)
class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product
    relationships. Includes homology and interaction.
    """

    _category: ClassVar[str] = 'GeneToGeneAssociation'


@dataclass(config=PydanticConfig)
class PairwiseGeneToGeneInteraction(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding)
    or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """

    _category: ClassVar[str] = 'PairwiseGeneToGeneInteraction'


@dataclass(config=PydanticConfig)
class NamedThingToInformationContentEntityAssociation(Association):
    """
    association between a named thing and a information content entity where the specific context
    of the relationship between that named thing and the publication is unknown. For
    example, model organisms databases often capture the knowledge that a gene is found in a
    journal article, but not specifically the context in which that gene was documented in the article.
    In these cases, this association with the accompanying predicate 'mentions' could be used.
    Conversely, for more specific associations (like 'gene to disease association', the publication should
    be captured as an edge property).
    """

    _category: ClassVar[str] = 'NamedThingToInformationContentEntityAssociation'


@dataclass(config=PydanticConfig)
class GeneToPhenotypicFeatureAssociation(Association):
    _category: ClassVar[str] = "GeneToPhenotypicFeatureAssociation"

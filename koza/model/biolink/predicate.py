"""
A lookup named tuple for Biolink edge types (or edge labels)
Note this should be generated from the biolink yaml
"""
from collections import namedtuple

predicates = [
    'actively_involved_in',
    'affected_by',
    'affects',
    'affects_abundance_of',
    'affects_activity_of',
    'affects_degradation_of',
    'affects_expression_in',
    'affects_expression_of',
    'affects_folding_of',
    'affects_localization_of',
    'affects_metabolic_processing_of',
    'affects_molecular_modification_of',
    'affects_mutation_rate_of',
    'affects_response_to',
    'affects_risk_for',
    'affects_secretion_of',
    'affects_splicing_of',
    'affects_stability_of',
    'affects_synthesis_of',
    'affects_transport_of',
    'affects_uptake_of',
    'ameliorates',
    'author',
    'biomarker_for',
    'capable_of',
    'caused_by',
    'causes',
    'causes_adverse_event',
    'chemically_similar_to',
    'close_match',
    'coexists_with',
    'coexpressed_with',
    'colocalizes_with',
    'condition_associated_with_gene',
    'contraindicated_for',
    'contributes_to',
    'contributor',
    'correlated_with',
    'decreases_abundance_of',
    'decreases_activity_of',
    'decreases_degradation_of',
    'decreases_expression_of',
    'decreases_folding_of',
    'decreases_localization_of',
    'decreases_metabolic_processing_of',
    'decreases_molecular_interaction',
    'decreases_molecular_modification_of',
    'decreases_mutation_rate_of',
    'decreases_response_to',
    'decreases_secretion_of',
    'decreases_splicing_of',
    'decreases_stability_of',
    'decreases_synthesis_of',
    'decreases_transport_of',
    'decreases_uptake_of',
    'derives_from',
    'derives_into',
    'develops_from',
    'directly_interacts_with',
    'disease_has_basis_in',
    'disrupted_by',
    'disrupts',
    'editor',
    'enabled_by',
    'enables',
    'exacerbates',
    'exact_match',
    'expressed_in',
    'expresses',
    'gene_associated_with_condition',
    'genetic_association',
    'genetically_interacts_with',
    'has_biomarker',
    'has_completed',
    'has_decreased_amount',
    'has_gene_product',
    'has_increased_amount',
    'has_input',
    'has_molecular_consequence',
    'has_not_completed',
    'has_output',
    'has_part',
    'has_participant',
    'has_phenotype',
    'has_sequence_location',
    'has_variant_part',
    'homologous_to',
    'in_cell_population_with',
    'in_complex_with',
    'in_linkage_disequilibrium_with',
    'in_pathway_with',
    'in_taxon',
    'increases_abundance_of',
    'increases_activity_of',
    'increases_degradation_of',
    'increases_expression_of',
    'increases_folding_of',
    'increases_localization_of',
    'increases_metabolic_processing_of',
    'increases_molecular_interaction',
    'increases_molecular_modification_of',
    'increases_mutation_rate_of',
    'increases_response_to',
    'increases_secretion_of',
    'increases_splicing_of',
    'increases_stability_of',
    'increases_synthesis_of',
    'increases_transport_of',
    'increases_uptake_of',
    'interacts_with',
    'is_frameshift_variant_of',
    'is_missense_variant_of',
    'is_nearby_variant_of',
    'is_non_coding_variant_of',
    'is_nonsense_variant_of',
    'is_sequence_variant_of',
    'is_splice_site_variant_of',
    'is_synonymous_variant_of',
    'lacks_part',
    'located_in',
    'location_of',
    'manifestation_of',
    'model_of',
    'molecularly_interacts_with',
    'negatively_correlated_with',
    'negatively_regulated_by_entity_to_entity',
    'negatively_regulated_by_process_to_process',
    'negatively_regulates_entity_to_entity',
    'negatively_regulates_process_to_process',
    'occurs_in',
    'orthologous_to',
    'overlaps',
    'paralogous_to',
    'part_of',
    'participates_in',
    'physically_interacts_with',
    'positively_correlated_with',
    'positively_regulated_by_entity_to_entity',
    'positively_regulated_by_process_to_process',
    'positively_regulates_entity_to_entity',
    'positively_regulates_process_to_process',
    'preceded_by',
    'precedes',
    'predisposes',
    'prevented_by',
    'prevents',
    'produced_by',
    'produces',
    'provider',
    'publisher',
    'regulated_by_entity_to_entity',
    'regulated_by_process_to_process',
    'regulates_entity_to_entity',
    'regulates_process_to_process',
    'related_condition',
    'related_to',
    'same_as',
    'similar_to',
    'subclass_of',
    'superclass_of',
    'temporally_related_to',
    'treated_by',
    'treats',
    'xenologous_to',
]

predicate = namedtuple('biolink_predicate', predicates)(
    *['biolink:' + predicate for predicate in predicates]
)
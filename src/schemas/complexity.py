from src.schemas import BaseSchema


class Complexity(BaseSchema):
    crawford: float
    gutierrez_polini: float
    szigriszt_pazos: float
    fernandez_huerta: float
    dale_chall_readability_score_v2: float
    dale_chall_readability_score: float
    linsear_write_formula: float
    automated_readability_index: float
    coleman_liau_index: float
    smog_index: int
    flesch_kincaid_grade: float
    flesch_reading_ease: float

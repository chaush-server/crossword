from textstat import textstat  # type: ignore


class AnalyzerService:
    @staticmethod
    async def get_text_complexity(raw_text: str) -> dict[str, float]:
        return {
            "crawford": textstat.crawford(raw_text),
            "gutierrez_polini": textstat.gutierrez_polini(raw_text),
            "szigriszt_pazos": textstat.szigriszt_pazos(raw_text),
            "fernandez_huerta": textstat.fernandez_huerta(raw_text),
            "dale_chall_readability_score_v2": textstat.dale_chall_readability_score_v2(
                raw_text
            ),
            "dale_chall_readability_score": textstat.dale_chall_readability_score(
                raw_text
            ),
            "linsear_write_formula": textstat.linsear_write_formula(raw_text),
            "automated_readability_index": textstat.automated_readability_index(
                raw_text
            ),
            "coleman_liau_index": textstat.coleman_liau_index(raw_text),
            "smog_index": textstat.smog_index(raw_text),
            "flesch_kincaid_grade": textstat.flesch_kincaid_grade(raw_text),
            "flesch_reading_ease": textstat.flesch_reading_ease(raw_text),
        }

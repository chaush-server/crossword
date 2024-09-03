from textstat import textstat  # type: ignore


class AnalyzerService:
    @staticmethod
    async def get_text_complexity(raw_text: str) -> float:
        return textstat.linsear_write_formula(raw_text)  # type: ignore

from abc import ABC, abstractmethod

class UserAnalysisQuestionRepository(ABC):
    @abstractmethod
    def create(self, user_analysis, question_text, user_analysis_type):
        pass
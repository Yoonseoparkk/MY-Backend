from account.entity.account import Account

from django.db import IntegrityError

from user_analysis.entity.user_analysis import UserAnalysis
from user_analysis.entity.user_analysis_answer import UserAnalysisAnswer
from user_analysis.entity.user_analysis_custom_selection import UserAnalysisCustomSelection
from user_analysis.entity.user_analysis_fixed_boolean_selection import UserAnalysisFixedBooleanSelection
from user_analysis.entity.user_analysis_fixed_five_score_selection import UserAnalysisFixedFiveScoreSelection
from user_analysis.repository.user_analysis_answer_repository import UserAnalysisAnswerRepository
from user_analysis.repository.user_analysis_question_repository_impl import UserAnalysisQuestionRepositoryImpl
from user_analysis.repository.user_analysis_repository_impl import UserAnalysisRepositoryImpl


class UserAnalysisAnswerRepositoryImpl(UserAnalysisAnswerRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__userAnalysisQuestionRepository = UserAnalysisQuestionRepositoryImpl.getInstance()
            cls.__instance.__userAnalysisRepository = UserAnalysisRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def saveAnswer(self, request, question, answer_data):
        try:

            if question.user_analysis_type == 1:  # General
                answer = UserAnalysisAnswer(
                    request=request,
                    question=question,
                    answer_text=answer_data,
                )

            elif question.user_analysis_type == 2:  # Five Score
                five_score_selection = UserAnalysisFixedFiveScoreSelection.objects.get(score=answer_data)
                answer = UserAnalysisAnswer(
                    request=request,
                    question=question,
                    five_score_selection=five_score_selection,
                )

            elif question.user_analysis_type == 3:  # Boolean
                boolean_selection = UserAnalysisFixedBooleanSelection.objects.get(is_true=answer_data)
                answer = UserAnalysisAnswer(
                    request=request,
                    question=question,
                    boolean_selection=boolean_selection,
                )

            elif question.user_analysis_type == 4:  # Custom
                custom_selection = UserAnalysisCustomSelection.objects.get(question = question, custom_text=answer_data)
                answer = UserAnalysisAnswer(
                    request=request,
                    question=question,
                    custom_selection=custom_selection,
                )

            answer.save()
            return answer

        except IntegrityError as e:
            raise IntegrityError(f"Error saving user_analysis answer: {e}")

    def summarizeAnswerByUserAnalysisId(self, user_analysis_id):
        summerizedAnswer = UserAnalysisAnswer.objects.filter(user_analysis_id=user_analysis_id)
        return summerizedAnswer

    def summarizeAnswerByQuestionId(self, question_id):
        summerizedAnswer = UserAnalysisAnswer.objects.filter(question_id=question_id)
        return summerizedAnswer

    def summarizeAnswerByAccountId(self, account_id):
        summerizedAnswer = UserAnalysisAnswer.objects.filter(account_id=account_id)
        return summerizedAnswer

    def summarizeAnswerByUserAnalysisIdandAccountId(self, user_analysis_id, account_id):
        summerizedAnswer = UserAnalysisAnswer.objects.filter(user_analysis_id=user_analysis_id, account_id=account_id)
        return summerizedAnswer

    def list(self):
        return UserAnalysisAnswer.objects.all()

    def findByRequest(self, request):
        return UserAnalysisAnswer.objects.filter(request = request)

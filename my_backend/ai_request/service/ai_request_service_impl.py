from ai_request.repository.ai_request_repository_impl import AiRequestRepositoryImpl
from ai_request.service.ai_request_service import AiRequestService


class AiRequestServiceImpl(AiRequestService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__aiRequestRepository = AiRequestRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def aiRequestToFastAPI(self, command, data):
        try:
            return self.__aiRequestRepository.aiRequest(command, data)
        except Exception as e:
            print('Error sending request to FastAPI:', e)
            raise e
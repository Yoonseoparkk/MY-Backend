from board.repository.board_repository_impl import BoardRepositoryImpl
from board.service.board_service import BoardService

class BoardServiceImpl(BoardService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__boardRepository = BoardRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def list(self):
        return self.__boardRepository.list()

    def createCategory(self, name):
        return self.__boardRepository.create_category(name)

    def createBoard(self, categoryId, title, accountId, content, contentImage):
        return self.__boardRepository.create(categoryId, title, accountId, content, contentImage)

    def readBoard(self, boardId):
        return self.__boardRepository.findByBoardId(boardId)

    def removeBoard(self, boardId):
        return self.__boardRepository.deleteByBoardId(boardId)

    def updateBoard(self, boardId, boardData):
        board = self.__boardRepository.findByBoardId(boardId)
        return self.__boardRepository.update(board, boardData)

    def get_all_categories(self):
        return list(self.__boardRepository.get_all_categories())

    def listByCategoryId(self, categoryId):
        return self.__boardRepository.listBoardByCategoryId(categoryId)

    def listByTitle(self, title):
        return self.__boardRepository.listBoardByTitle(title)

    def listByContent(self, content):
        return self.__boardRepository.listBoardByContent((content))




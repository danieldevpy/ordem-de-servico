from src.application.repository.pageRepository import PageRepository

class Routes:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            return cls._instance
        else:
            return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, 'pages'):
            self.pages = {
                'selected': None,
                'welcome': None,
            }

    def config_welcome(self, page_welcome: PageRepository=None):
        self.pages['selected'] = page_welcome
        self.pages['welcome'] = page_welcome
        self.pages['selected'].assemble()

    def register_page(self, name_route: str, page: PageRepository):
        self.pages[name_route] = page

    def navigate(self, name_route: str, option=None):
        self.pages['selected'].disassemble()
        page: PageRepository = self.pages[name_route]
        self.pages['selected'] = page
        if not option:
            page.assemble()
        else:
            page.assemble(option)

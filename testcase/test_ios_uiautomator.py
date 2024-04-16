from Base.get_driver import GetDriver_u2
from Base.init_driver import init_driver_ios_ui2
from PagesUI.page_element_ios import CommonElementIos


class test_ios:
    def __init__(self):
        self.driver = GetDriver_u2().create_driver(init_driver_ios_ui2())
        self.el = CommonElementIos()

    def test_star_app(self):
        self.driver.open_app('com.starmakerapp.starmaker')


test_ios().test_star_app()

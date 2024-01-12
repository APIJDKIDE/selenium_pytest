import ordering as ordering
import pytest
from pages.homepage.home_page import homePage


class TestGoToHomePage():

    #@pytest.mark.skip
    def test_goto_homepage(self):
        homepage = homePage()
        homepage.goto_homePage()

    #@pytest.mark.skip
    #@pytest.mark.parametrize('userName',['liuww1','luozz','liangrx3','wenxq'])
    def test_SimulationLogin(self):
        homepage = homePage()
        homepage.simulationLogin("liuww1")

    @pytest.mark.skip
    def test_clickLanguage(self):
        homepage = homePage()
        homepage.click_clickLanguage()
    @pytest.mark.skip
    def test_clickProjectManagement(self):
        homepage = homePage()
        homepage.click_clickProjectManagement()



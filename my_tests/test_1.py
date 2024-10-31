import pytest


class LoginTest:
    def test_if_login_correct(self):
        # todo: clean: delete mainmagic, delete unittest methods, import from base_page

        x = MainMagic()
        x.start()
        x.correct_login()

        # expected url = inventory page because this is where we should land after successful login,
        # and it's accessible only if we are logged in.
        expected_url = "https://www.saucedemo.com/inventory.html"
        current_url = x.current_url()
        self.assertEqual(current_url, expected_url)

        '''class LoginTest(unittest.TestCase):
            def test_if_login_correct(self):
                x = MainMagic()
                x.start()
                x.correct_login()

                # expected url = inventory page because this is where we should land after successful login,
                # and it's accessible only if we are logged in.
                expected_url = "https://www.saucedemo.com/inventory.html"
                current_url = x.current_url()
                self.assertEqual(current_url, expected_url)'''
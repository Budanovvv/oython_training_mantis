class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user, password):
        wd = self.app.wd
        self.app.main_url()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(user)
        wd.find_element_by_css_selector('input[type="submit"]').click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector('input[type="submit"]').click()

    def ensure_login(self, user, password):
        if self.is_logged_in():
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user, password)

    def get_logged_user_name(self):
        wd = self.app.wd
        return wd.find_element_by_xpath('//*[@id="breadcrumbs"]/ul/li/a').text

    def is_logged_in_as(self, user):
        return self.get_logged_user_name() == user

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('i[class="fa fa-angle-down ace-icon"]').click()
        wd.find_element_by_css_selector('a[href="/mantisbt-2.25.2/logout_page.php"]').click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

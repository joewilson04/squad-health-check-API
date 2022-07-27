from django.contrib.auth.views import LoginView
from django.contrib.auth.backends import BaseBackend





class squad_loginView(LoginView):
    template_name = 'squad/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or '/squad/profile'

class scrum_loginView(LoginView):
    template_name = 'scrum/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or '/scrum/profile'

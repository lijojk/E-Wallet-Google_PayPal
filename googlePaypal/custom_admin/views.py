from django.contrib.auth.views import LoginView
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    template_name = 'adloggoogle/templates/admin/mainindex.html'  # Path to your custom login template

    def get_success_url(self):
        return '/admin'  # Redirect to the desired admin home page
        # return 'admin/adlogin.html'

    def form_valid(self, form):
        # Perform any custom login logic here (e.g., additional checks or actions)

        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        # Redirect authenticated users to the admin home page if they try to access the login page
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())

        return super().get(request, *args, **kwargs)



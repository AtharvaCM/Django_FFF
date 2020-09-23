from django.test import TestCase, SimpleTestCase
from fff import views as views
import django.contrib.auth.views as auth_views
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('freshfromfarm-home')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, views.index)

    def test_about_url_is_resolved(self):
        url = reverse('freshfromfarm-about')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, views.about)

    def test_contact_url_is_resolved(self):
        url = reverse('freshfromfarm-contact')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, views.contact)

    def test_services_url_is_resolved(self):
        url = reverse('freshfromfarm-services')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, views.services)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, views.register)

    def test_activate_url_is_resolved(self):
        url = reverse('activate', args=['uidb64', 'token'])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, views.activate)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)

    def test_view_profile_url_is_resolved(self):
        url = reverse('view_profile')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, views.view_profile)

    def test_edit_profile_url_is_resolved(self):
        url = reverse('edit_profile')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, views.edit_profile)

    def test_password_change_url_is_resolved(self):
        url = reverse('password_change')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,
                          auth_views.PasswordChangeView)

    def test_password_change_done_url_is_resolved(self):
        url = reverse('password_change_done')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,
                          auth_views.PasswordChangeDoneView)

    def test_password_reset_url_is_resolved(self):
        url = reverse('password_reset')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,
                          auth_views.PasswordResetView)

    def test_password_reset_confirm_url_is_resolved(self):
        url = reverse('password_reset_confirm', args=['uidb64', 'token'])
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,
                          auth_views.PasswordResetConfirmView)

    def test_password_reset_done_url_is_resolved(self):
        url = reverse('password_reset_done')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,
                          auth_views.PasswordResetDoneView)

    def test_password_reset_complete_url_is_resolved(self):
        url = reverse('password_reset_complete')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,
                          auth_views.PasswordResetCompleteView)

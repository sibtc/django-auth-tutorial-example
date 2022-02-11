from django.contrib import admin
from django.urls import path, include

from mysite.core import views

from searchapp import views as searchapp_views


urlpatterns = [
	path('', views.home, name='home'),
	path('signup/', views.signup, name='signup'),
	path('secret/', views.secret_page, name='secret'),
	path('secret2/', views.SecretPage.as_view(), name='secret2'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('admin/', admin.site.urls),

	# searchapp
	path('book-list/', searchapp_views.book_list, name='book_list'),

	path('book-detail/<id>', searchapp_views.book_detail, name='book_detail'),

	path('search/', searchapp_views.search, name='search'),
]

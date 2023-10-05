from django.urls import path
from AppCoderhouse.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('about/', about, name="About"),
    path('buscar-articulos/', busqueda_articulo, name='BuscarArticulos'),
    path('buscar/', buscar, name='Buscar'),
    path('signup/', SignUp.as_view(), name="Signup"),
    path('login/', Login.as_view(), name="Login"),
    path('logout/', Logout.as_view(), name="Logout"),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name="profile-update"),
    path('profile/create', ProfileCreate.as_view(), name="profile-create"),
    path('profile/<pk>/detail', ProfileDetail.as_view(), name="profile-detail"),
    path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create"),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list"),
    path('product/list', ProductList.as_view(), name="product-list"),
    path('product/<pk>/detail', ProductDetail.as_view(), name="product-detail"),
    path('product/create', ProductCreate.as_view(), name="product-create"),
    path('product/<pk>/update', ProductUpdate.as_view(), name="product-update"),
    path('product/<pk>/delete', ProductDelete.as_view(), name="product-delete"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
from django.urls import path
from AppBlog.views import inicio, cafe, platos, postres, quesos, vinos

urlpatterns = [

    path('inicio/', inicio, name='inicio'),
    path('cafe/', cafe, name='cafe'),
    path('platos/', platos, name='platos'),
    path('postres/', postres, name='postres'),
    path('quesos/', quesos, name='quesos'),
    path('vinos/', vinos, name='vinos'),
]
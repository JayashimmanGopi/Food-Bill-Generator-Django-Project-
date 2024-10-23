from django.urls import path
from hotel.views import CreateView, homepage, detailpage, UpdateView,deleteview,login_view, signup_view, logout_view

urlpatterns = [
    
    path('home/', homepage, name="homepage"),
    path('detail/<int:id>', detailpage, name="detailpage"), 
    path('create/', CreateView, name='createview'), 
    path('update/<int:id>', UpdateView, name='updateview'),
    path('delete/<int:id>',deleteview,name='deleteview'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
]




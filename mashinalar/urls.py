from django.urls import path
from .views import CarList,CarCreate,CarDelete,CarUpdate,CarDetail

urlpatterns=[
    path('list/',CarList.as_view()),
    path('create/',CarCreate.as_view()),
    path('delete/<int:pk>/',CarDelete.as_view()),
    path('edit/<int:pk>/',CarUpdate.as_view()),
    path('detail/<int:pk>/',CarDetail.as_view()),
]
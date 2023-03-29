from django.urls import path
from . import views

urlpatterns = [
    path('myaccount/', views.ViewAccount.as_view()),
    path('myaccount/<int:id>', views.ViewAccountFromURL.as_view()),
    path('transaction/', views.ViewTransaction.as_view()),
    path('transaction/<int:id>', views.ViewTransactionFromURL.as_view()),
]
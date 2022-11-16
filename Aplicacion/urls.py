from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('products/', views.products, name="especialidad"),
    path('registrarEspecialidad/', views.registrarEspecialidad),

    path('pacienten/', views.pacienten, name="pacienten"),
    path('registrarPaciente/', views.registrarPaciente),
    
    path('customer/<str:pk_test>/', views.customer, name="paciente"),

    path('crear_cita/', views.crearCita, name="crear_cita"),
    path('actualizar_cita/<str:pk>/', views.actualizarCita, name="actualizar_cita"),
    path('eliminar_cita/<str:pk>/', views.eliminarCita, name="eliminar_cita"),
]

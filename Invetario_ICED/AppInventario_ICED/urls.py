from django.urls import path
from . import viewsLogin 
from .views import *
from . import views
from django.conf import *
from django.conf.urls.static import *
from django.contrib.auth import views as auth_views
from django.urls import path, reverse
from . viewsLogin import *
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView 
import jwt 



urlpatterns=[   

    #VALIDACION FLUTTER
    path('verificarS', viewsLogin.verificarS, name='verificarS'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Ruta para obtener el token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Ruta para refrescar el token JWT
     
    
    #PORTADA PRINCIPAL
    path('Principal',Portada,name="Principal"),
    path('Informacion',Informacion,name='Informacion'),
    path('Nosotros',Nosotros,name='Nosotros'),
    path('RecuperarContraseña',RecuperarContraseña,name='Recuperarcontraseña'),
    
    
    
    path('VistasUsuarios',VistasUsuarios,name="VistaUsarios"),
    path('listar_datos/', views.ListadoDatos.as_view(), name='listar_datos'),
    
    #LOGIN
    path('registro/',RegistrarUsuarioView.as_view(),name="registrar_usuario"),
    path('iniciarSesion/',IniciarSesionView.as_view(),name="iniciar_sesion"),
    path('ActualizarUsuario/',PerfilClienteView.as_view(),name="perfil_usuario"),
    path('Login',views.Login,name='Login'),
    path('VistasUsuarios',VistasUsuarios,name="VistaUsarios"),

    #LOGOUT 
    path('logout/', views.user_logout, name='logout'),


    #recuperar contraseña mediante correo

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),




    #FORMULARIO
    path('Formulario',views.Formulario,name='Formulario'),
    #CRUD EQUIPOS
    path('Equipo',views.Equipo,name='Equipo'),
    path('ListarEquipos',ListadoEquipos.as_view(),name='ListarEquipos'),
    path('insertar/',InsertarEquipos.as_view(),name='insertar'),
    path('ActualizarEquipo/<int:pk>',ActualizarEquipo.as_view(),name='actualizar'),
    path('EliminarEquipo/<int:pk>',EliminarEquipo.as_view(),name='eliminar'),    
    path('BuscarEquipo/<str:equi_serial>/', views.BuscarEquipo.as_view(), name='buscar_equipo'),
    path('BuscarEquipoID/<int:pk>', BuscarEquipoID.as_view(), name='buscar-equipo'),
    path('ContarEquipos', ContarEquipos.as_view(), name='contar-equipos'),
    path('ContarActivos', ContarActivos.as_view(), name='contar-activos'),
    path('ContarInactivos', ContarInactivos.as_view(), name='contar-inactivos'),
    #CRUD USUARIOS
    path('Usuario',views.Usuario,name='Usuario'),
    path('ListarUsuarios', ListarUsuarios.as_view(), name='ListarUsuarios'),
    path('insertarUsuario/', InsertarUsuarios.as_view(), name='insertarUsuario'),
    path('formularioInsertar',views.Formulario,name="insertarf"),
    path('ActualizarUsuario/<int:pk>', ActualizarUsuarios.as_view(), name='actualizarUsuario'),
    path('EliminarUsuario/<int:pk>', EliminarUsuario.as_view(), name='eliminarUsuario'),
    path('BuscarUsuario/<int:pk>', views.BuscarUsuario.as_view(), name='buscarUsuario'),  # Nueva ruta
    path('ContarUsuarios', ContarUsuarios.as_view(), name='cantidad_usuarios'),
    path('ContarAprendices', ContarAprendices.as_view(), name='cantidad_aprendices'),
    path('ContarInstructores',ContarInstructor.as_view(), name='cantidad_instructores'),
    
    #CRUD PRESTAMOS
    path('Prestamo',views.Prestamo,name='Prestamo'),
    path('ListarPrestamos',ListadoPrestamos.as_view(),name='Prestamos'),
    path('insertarPrestamo/',InsertarPrestamos.as_view(),name='insertarPrestamo'),
    path('ActualizarPrestamo/<int:pk>',ActualizarPrestamo.as_view(),name='actualizarPrestamo'),
    path('BuscarPrestamo/<int:pk>', BuscarPrestamo.as_view(), name='buscar-prestamo'),
    path('EliminarPrestamo/<int:pk>',EliminarPrestamo.as_view(),name='eliminarPrestamo'),
    path('verificarPrestamo/', VerificarPrestamo.as_view(), name='verificar-prestamo'),
    path('ContarPrestamos', ContarPrestamos.as_view(), name='cantidad_prestamos'),
    path('contar_en_prestamo/', ContarEnPrestamo.as_view(), name='contar_en_prestamo'),


    #CRUD SANCIONES
    path('Sancion',views.Sancion,name='Sancion'),
    path('ListarSanciones',ListarSanciones.as_view(),name='Sanciones'),
    path('insertarSancion/',InsertarSanciones.as_view(),name='insertar'),
    path('ActualizarSanciones/<pk>',ActualizarSanciones.as_view(),name='Actualizar'),
    path('EliminarSancion/<pk>',EliminarSanciones.as_view(),name='Eliminar'),
    path('BuscarSancion/<int:pk>/', BuscarSancion.as_view(), name='buscar_sancion'),
    path('Totalsanciones/', ContarSanciones.as_view(), name='contar_sanciones'),  # Agregar esta línea
    #HISTORIAL
    path('Historial',views.historial,name='Historial'),
    path('Listarhistorial/',ListarHistorial.as_view(), name='Historia'),
    path('EliminarHistorial/<int:pk>',EliminarHistorial.as_view(),name='eliminarHistorial'),
    path('BuscarHistorial/<int:pk>', BuscarHistorial.as_view(), name='buscar-historial'),
    #subir excel
    path('subir_excel/', views.subir_excel, name='subir_excel'),

] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""" path('index.html',listadoEquipos.as_view(),name='Equipos'),
    path('indexuno.html',listadoUsuarios.as_view(),name='Usuarios'),
    path('indexdos.html',listadoPrestamos.as_view(),name='Prestamos'),
    path('indextres.html',listadoSanciones.as_view(),name='Sanciones'),
"""
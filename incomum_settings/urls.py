
from django.contrib import admin
from django.urls import path
from incomum import views
from django.contrib.auth.views import LogoutView
from incomum_settings import settings
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('teste/',views.logado,name='logado'),
    path('teste/logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('agencia/logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('agente/logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('agencia/',views.agencia,name='agencia'),
    path('relacao/<int:age_codigo>/',views.relacao,name='relacao'),
    path('agente/',views.agente,name='agente'),
    path('tst/',views.obter_novos_cadastros,name='obter_novos_cadastros'),
    path('consulta/',views.sua_view_de_consulta,name='consulta'),
    path('cep/', views.autocomplete_endereco, name='autocomplete_endereco'),
    path('excluir/<int:age_codigo>/', views.excluir_cadastro, name='excluir_cadastro'),
    path('faturamento/', views.faturamento, name='faturamento'),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('consulta_relatorio/', views.consulta_relatorio, name='consulta_relatorio'),
    path('exportar_excel/', views.exportar_excel, name='exportar_excel'),
]




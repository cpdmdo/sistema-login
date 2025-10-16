from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views 

# Importe todas as Views e Formulários
from app_usuario.views import tela_bem_vindo, cadastro_usuario 
from app_usuario.forms import FormularioLoginCustomizado 


urlpatterns = [
    # ... suas outras rotas ...

]


urlpatterns = [
    # 1. Admin
    path('admin/', admin.site.urls),
    

    path('cria-admin/', name='cria_admin_temp'), # ROTA TEMPORÁRIA

    # 2. Login (Customizado)
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True,
        authentication_form=FormularioLoginCustomizado 
    ), name='login'),
    
    # 3. Logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    
    # 4. Cadastro
    path('cadastro/', cadastro_usuario, name='cadastro'), 
    
    # ⚡️ 5. Página de Boas-Vindas ⚡️
    path('bem_vindo/', tela_bem_vindo, name='bem_vindo'),
    
    # ⚡️ 6. (OPCIONAL/SUGESTÃO): Rota Raiz (/) ⚡️
    # Para evitar que o Django tente carregar o / (raiz) e falhe, podemos redirecionar:
    # Esta linha garante que, ao acessar http://127.0.0.1:8000/, você vá para o login
    path('', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=FormularioLoginCustomizado 
    ), name='home'),
]
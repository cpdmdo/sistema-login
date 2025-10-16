from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Certifique-se de que esta importação está correta se você a moveu para o forms.py
from .forms import CadastroUsuarioForm 

# View Protegida (já existe)
@login_required 
def tela_bem_vindo(request):
    contexto = {
        'usuario': request.user.username 
    }
    return render(request, 'app_usuario/bem_vindo.html', contexto)

# ⚡️ ESTA FUNÇÃO DEVE ESTAR PRESENTE! ⚡️
def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login') 
    else:
        form = CadastroUsuarioForm()
        
    contexto = {'form': form}
    return render(request, 'app_usuario/cadastro.html', contexto)
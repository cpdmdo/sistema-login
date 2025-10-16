from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Importe o AuthenticationForm


# Nosso formulário de cadastro (já existe)
class CadastroUsuarioForm(UserCreationForm):
    pass


# ⚡️ NOVO: Formulário customizado para o Login ⚡️
class FormularioLoginCustomizado(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 1. Altera o Label (Descrição) do campo Username
        self.fields["username"].label = "E-mail"
        # Dica: O campo password é 'password'
        self.fields["password"].label = "Senha"

        # 2. Pode-se adicionar um placeholder aqui também!
        self.fields["username"].widget.attrs.update(
            {"placeholder": "Digite seu e_mail"}
        )
        self.fields["password"].widget.attrs.update({"placeholder": "Sua senha"})

from ninja import Router, UploadedFile, File
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
from .models import User, Profile
from .schemas import UserIn, UserOut, ProfileOut, LoginIn, TokenOut
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from ninja.security import HttpBearer
from django.contrib.auth import authenticate
from django.db import IntegrityError

router = Router(tags=["Usuários"])

# Autenticação JWT
class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            user = User.objects.get(id=request.user.id)
            return user
        except User.DoesNotExist:
            raise HttpError(401, "Token inválido ou expirado")

# Registro de usuário
@router.post(
    "/register/",
    response={201: UserOut, 400: dict},
    summary="Registrar usuário",
    description="Cria um novo usuário com os dados fornecidos.",
)
def register(request, payload: UserIn):
    try:
        payload_dict = payload.dict()
        payload_dict["password"] = make_password(payload.password)  # Criptografa a senha
        user = User.objects.create(**payload_dict)
        return 201, user
    except IntegrityError as e:
        raise HttpError(400, {"detail": "Erro ao criar usuário. Verifique os dados fornecidos."})
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Login de usuário
@router.post(
    "/login/",
    response={200: TokenOut, 401: dict},
    summary="Autenticar usuário",
    description="Autentica um usuário e retorna tokens JWT.",
)
def login(request, payload: LoginIn):
    user = authenticate(username=payload.username, password=payload.password)
    if user:
        refresh = RefreshToken.for_user(user)
        return 200, {"refresh": str(refresh), "access": str(refresh.access_token)}
    raise HttpError(401, {"detail": "Credenciais inválidas"})

# Perfil do usuário
@router.get(
    "/profile/",
    response={200: ProfileOut, 404: dict},
    summary="Perfil do usuário",
    description="Retorna o perfil do usuário autenticado.",
    auth=AuthBearer(),
)
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        return 200, profile
    except Profile.DoesNotExist:
        raise HttpError(404, {"detail": "Perfil não encontrado"})

# Listar todos os usuários
@router.get(
    "/usuarios/",
    response=list[UserOut],
    summary="Listar usuários",
    description="Retorna uma lista de todos os usuários cadastrados.",
    auth=AuthBearer(),
)
def listar_usuarios(request):
    return User.objects.all()

# Detalhes de um usuário
@router.get(
    "/usuarios/{usuario_id}/",
    response={200: UserOut, 404: dict},
    summary="Detalhes do usuário",
    description="Retorna os detalhes de um usuário específico.",
    auth=AuthBearer(),
)
def detalhes_usuario(request, usuario_id: int):
    usuario = get_object_or_404(User, id=usuario_id)
    return 200, usuario

# Atualizar um usuário
@router.put(
    "/usuarios/{usuario_id}/",
    response={200: UserOut, 400: dict, 404: dict},
    summary="Atualizar usuário",
    description="Atualiza os dados de um usuário existente.",
    auth=AuthBearer(),
)
def atualizar_usuario(request, usuario_id: int, payload: UserIn):
    usuario = get_object_or_404(User, id=usuario_id)
    try:
        for field, value in payload.dict().items():
            if value is not None:
                if field == "password":
                    value = make_password(value)  # Criptografa a nova senha
                setattr(usuario, field, value)
        usuario.save()
        return 200, usuario
    except IntegrityError as e:
        raise HttpError(400, {"detail": "Erro ao atualizar usuário. Verifique os dados fornecidos."})
    except Exception as e:
        raise HttpError(400, {"detail": str(e)})

# Excluir um usuário
@router.delete(
    "/usuarios/{usuario_id}/",
    response={204: None, 404: dict},
    summary="Excluir usuário",
    description="Exclui um usuário existente.",
    auth=AuthBearer(),
)
def excluir_usuario(request, usuario_id: int):
    usuario = get_object_or_404(User, id=usuario_id)
    usuario.delete()
    return 204, None
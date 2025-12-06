# Django
from rest_framework import viewsets

# Django Rest
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Models
from expenses.models import ExpenseMonth, ExpenseType, ExpenseBudget, ExpensePayment

# Serializers
from .serializers import (
    ExpenseMonthSerializer,
    ExpenseTypeSerializer,
    ExpenseBudgetSerializer,
    ExpensePaymentSerializer,
)

# Permissions
from .permissions import IsInGroup, user_group_actions

# ViewSets
class ExpenseMonthViewSet(viewsets.ModelViewSet):
    queryset = ExpenseMonth.objects.all()
    serializer_class = ExpenseMonthSerializer
    http_method_names = ["get", "post", "put", "patch"]
    required_groups = ["admin"]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """
        Retorna o queryset filtrado com base nas permissões do usuário.
        Esta lógica se aplica automaticamente a list() e retrieve().
        """
        user = self.request.user
        user_groups = [group.name for group in user.groups.all()]
        
        # 1. Superuser: Vê todos os objetos
        if user.is_superuser:
            return self.queryset.all()

        # 2. Usuário no grupo "user": Vê apenas seus próprios objetos
        elif "user" in user_groups:
            # Filtra o queryset para incluir apenas despesas do usuário logado
            return self.queryset.filter(fk_user_id=user.id)
            
        # 3. Outros casos (sem permissão): Retorna um queryset vazio
        # Isso resultará em 404 (Not Found) para retrieve e lista vazia para list
        return self.queryset.none()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def perform_create(self, serializer):
        # Passa o parâmetro fk_user_id de acordo com o usuário que fez a requisição.
        serializer.save(fk_user_id=self.request.user)
    
    def perform_update(self, serializer):
        # Passa o parâmetro fk_user_id de acordo com o usuário que fez a requisição.
        serializer.save(fk_user_id=self.request.user)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class ExpenseTypeViewSet(viewsets.ModelViewSet):
    queryset = ExpenseType.objects.all()
    serializer_class = ExpenseTypeSerializer
    http_method_names = ["get", "post", "put", "patch"]
    required_groups = ["user"]
    permission_classes = [IsAuthenticated, IsInGroup]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """
        Retorna o queryset filtrado com base nas permissões do usuário.
        Esta lógica se aplica automaticamente a list() e retrieve().
        """
        user = self.request.user
        user_groups = [group.name for group in user.groups.all()]
        
        # 1. Superuser: Vê todos os objetos
        if user.is_superuser:
            return self.queryset.all()

        # 2. Usuário no grupo "user": Vê apenas seus próprios objetos
        elif "user" in user_groups:
            # Filtra o queryset para incluir apenas despesas do usuário logado
            return self.queryset.filter(fk_user_id=user.id)
            
        # 3. Outros casos (sem permissão): Retorna um queryset vazio
        # Isso resultará em 404 (Not Found) para retrieve e lista vazia para list
        return self.queryset.none()

    def get_permissions(self):
        if self.action in user_group_actions:
            return [IsAuthenticated()]  # User permissions

        # Default controller
        return super().get_permissions()

    @action(detail=False, url_path="user", methods=["get"])
    def by_user(self, request):
        queryset = self.queryset.filter(fk_user_id=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        # Passa o parâmetro fk_user_id de acordo com o usuário que fez a requisição.
        serializer.save(fk_user_id=self.request.user)
    
    def perform_update(self, serializer):
        # Passa o parâmetro fk_user_id de acordo com o usuário que fez a requisição.
        serializer.save(fk_user_id=self.request.user)


class ExpenseBudgetViewSet(viewsets.ModelViewSet):
    queryset = ExpenseBudget.objects.all()
    serializer_class = ExpenseBudgetSerializer
    http_method_names = ["get", "post", "put", "patch"]
    required_groups = ["user"]
    permission_classes = [IsAuthenticated, IsInGroup]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """
        Retorna o queryset filtrado com base nas permissões do usuário.
        Esta lógica se aplica automaticamente a list() e retrieve().
        """
        user = self.request.user
        user_groups = [group.name for group in user.groups.all()]
        
        # 1. Superuser: Vê todos os objetos
        if user.is_superuser:
            return self.queryset.all()

        # 2. Usuário no grupo "user": Vê apenas seus próprios objetos
        elif "user" in user_groups:
            # Filtra o queryset para incluir apenas despesas do usuário logado
            return self.queryset.filter(fk_user_id=user.id)
            
        # 3. Outros casos (sem permissão): Retorna um queryset vazio
        # Isso resultará em 404 (Not Found) para retrieve e lista vazia para list
        return self.queryset.none()

    def get_permissions(self):
        if self.action in user_group_actions:
            return [IsAuthenticated()]  # User permissions

        # Default controller
        return super().get_permissions()

    @action(detail=False, url_path="user", methods=["get"])
    def by_user(self, request):
        queryset = self.queryset.filter(fk_user_id=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        # Passa o parâmetro fk_user_id de acordo com o usuário que fez a requisição.
        serializer.save(fk_user_id=self.request.user)
    
    def perform_update(self, serializer):
        # Passa o parâmetro fk_user_id de acordo com o usuário que fez a requisição.
        serializer.save(fk_user_id=self.request.user)


class ExpensePaymentViewSet(viewsets.ModelViewSet):
    queryset = ExpensePayment.objects.all()
    serializer_class = ExpensePaymentSerializer
    http_method_names = ["get", "post", "put", "patch"]
    required_groups = ["user"]
    permission_classes = [IsAuthenticated, IsInGroup]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """
        Retorna o queryset filtrado com base nas permissões do usuário.
        Esta lógica se aplica automaticamente a list() e retrieve().
        """
        user = self.request.user
        user_groups = [group.name for group in user.groups.all()]
        
        # 1. Superuser: Vê todos os objetos
        if user.is_superuser:
            return self.queryset.all()

        # 2. Usuário no grupo "user": Vê apenas seus próprios objetos
        elif "user" in user_groups:
            # Filtra o queryset para incluir apenas despesas do usuário logado
            return self.queryset.filter(fk_user_id=user.id)
            
        # 3. Outros casos (sem permissão): Retorna um queryset vazio
        # Isso resultará em 404 (Not Found) para retrieve e lista vazia para list
        return self.queryset.none()

    def get_permissions(self):
        if self.action in user_group_actions:
            return [IsAuthenticated()]  # User permissions

        # Default controller
        return super().get_permissions()

    @action(detail=False, url_path="user", methods=["get"])
    def by_user(self, request):
        queryset = self.queryset.filter(fk_user_id=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        # Passa o parâmetro fk_user_id de acordo com o usuário que fez a requisição.
        serializer.save(fk_user_id=self.request.user)
    
    def perform_update(self, serializer):
        # Passa o parâmetro fk_user_id de acordo com o usuário que fez a requisição.
        serializer.save(fk_user_id=self.request.user)
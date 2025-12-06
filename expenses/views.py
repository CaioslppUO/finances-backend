# Django
from rest_framework import viewsets, status

# Django Rest
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication

# Models
from expenses.models import ExpenseType, ExpenseBudget, ExpensePayment, Expense

# Serializers
from .serializers import (
    ExpenseTypeSerializer,
    ExpenseBudgetSerializer,
    ExpensePaymentSerializer,
    ExpenseSerializer
)

# Filtros
from .filters import ExpenseFilter

# Permissions
from .permissions import IsInGroup, user_group_actions

# ViewSets
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

    def perform_create(self, serializer):
        # Passa o parâmetro fk_user_id de acordo com o usuário que fez a requisição.
        serializer.save(fk_user_id=self.request.user)
    
    def perform_update(self, serializer):
        # Passa o parâmetro fk_user_id de acordo com o usuário que fez a requisição.
        serializer.save(fk_user_id=self.request.user)

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    required_groups = ["user"]
    permission_classes = [IsAuthenticated, IsInGroup]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend] 
    filterset_class = ExpenseFilter

    def get_queryset(self):
        """
        Retorna o queryset filtrado com base nas permissões do usuário.
        Esta lógica se aplica automaticamente a list() e retrieve().
        """
        user = self.request.user
        user_groups = [group.name for group in user.groups.all()]
    
        # 1. Superuser: Vê todos os objetos
        if user.is_superuser:
            queryset = self.queryset.all()
        # 2. Usuário no grupo "user": Vê apenas seus próprios objetos
        elif "user" in user_groups:
            # Filtra o queryset para incluir apenas despesas do usuário logado
            queryset = self.queryset.filter(fk_user_id=user.id)
        else:
            return self.queryset.none()
            
        # 3. Outros casos (sem permissão): Retorna um queryset vazio
        # Isso resultará em 404 (Not Found) para retrieve e lista vazia para list
        return queryset

    def get_permissions(self):
        if self.action in user_group_actions:
            return [IsAuthenticated()]  # User permissions

        # Default controller
        return super().get_permissions()

    def perform_create(self, serializer):
        # Passa o parâmetro fk_user_id de acordo com o usuário que fez a requisição.
        serializer.save(fk_user_id=self.request.user)
    
    def perform_update(self, serializer):
        # Passa o parâmetro fk_user_id de acordo com o usuário que fez a requisição.
        serializer.save(fk_user_id=self.request.user)

    @action(detail=False, methods=['get'])
    def year(self, request, pk=None):
        """
        Retorna, por mês, no período de um ano (janeiro a dezembro), todas as despesas.
        """
        year = request.query_params.get("year")
        if not year:
            return Response({"error": "O parâmetro 'year' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            int(year)
        except ValueError:
            return Response({"error": "O parâmetro 'year' deve ser um número inteiro."}, status=status.HTTP_400_BAD_REQUEST)

        expenses = self.get_queryset().filter(date__year=year).all() 
        
        # Vetor com 12 posições: 0 = Janeiro, 11 = Dezembro.
        expenses_by_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        for expense in expenses:
            month = expense.date.month
            expenses_by_month[month-1] = round(expenses_by_month[month-1] + float(expense.value), 2)

        return Response(expenses_by_month)
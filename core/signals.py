from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group
from django.dispatch import receiver


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    """
    Cria grupos padrão após migrações, caso ainda não existam.
    Create default user groups after migrations, if they do not already exists.
    """
    default_groups = ["admin", "user"]

    for group_name in default_groups:
        Group.objects.get_or_create(name=group_name)

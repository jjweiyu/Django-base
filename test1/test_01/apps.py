from django.apps import AppConfig


class Test01Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_01'
    # reset admin's book to 书籍管理
    verbose_name = "书籍管理"

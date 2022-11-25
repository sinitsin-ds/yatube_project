from django.contrib import admin

from .models import Post
from .models import Group

class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    # Добавляем возможность изменять поле group из списка постов
    list_editable = ('group',) 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка 
    empty_value_display = '-пусто-'  
    

# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Group)  
admin.site.register(Post, PostAdmin)
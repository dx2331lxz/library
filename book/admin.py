from django.contrib import admin

# Register your models here.
admin.site.site_header = '图书管理系统'  # 设置header
admin.site.site_title = '图书管理系统'  # 设置title
admin.site.index_title = '图书管理系统'  # 设置首页title

from .models import Book


# 注册小区表
class BookAdmin(admin.ModelAdmin):
    # 新增和修改页面需要展示的字段
    fields = ('name', 'price', 'author', 'publish', 'pub_date')

    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['name', 'price', 'author', 'publish', 'pub_date']

    # 搜索
    search_fields = ['name', 'price', 'author', 'publish']

    # 只读字段
    # readonly_fields = ('code', 'create_time', 'update_time')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 5

    # ordering设置默认排序字段，负号表示降序排序
    # ordering = ('-create_time',)

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('name', 'price', 'author', 'publish', 'pub_date')
    # 详细时间分层筛选　
    # date_hierarchy = 'create_time'

    # list_editable 设置默认可编辑字段，这个字段必须要在list_display里面配置才可以使用
    # 并且必须表里面有对应字段，不能是自己定义的列表字段
    # list_editable = ['']

    # fk_fields 设置显示外键字段,如果这个表里面有外键，并且想要在列表展示，就可以使用这个配置
    # fk_fields = ('',)


admin.site.register(Book, BookAdmin)
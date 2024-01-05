from django.contrib import admin
from .models import Borrow
import datetime


# Register your models here.


class BorrowAdmin(admin.ModelAdmin):
    # 新增和修改页面需要展示的字段
    fields = ('book', 'user', 'is_return', 'is_overdue')

    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['book', 'user', 'borrow_time', 'return_time', 'is_return', 'is_overdue']

    # 搜索
    search_fields = ['book', 'user', 'is_return', 'is_overdue']

    # 只读字段
    # readonly_fields = ('code', 'create_time', 'update_time')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 5

    # ordering设置默认排序字段，负号表示降序排序
    # ordering = ('-create_time',)

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('book', 'user', 'borrow_time', 'return_time', 'is_return', 'is_overdue')

    # 详细时间分层筛选　
    # date_hierarchy = 'create_time'

    # list_editable 设置默认可编辑字段，这个字段必须要在list_display里面配置才可以使用
    # 并且必须表里面有对应字段，不能是自己定义的列表字段
    # list_editable = ['']

    # fk_fields 设置显示外键字段,如果这个表里面有外键，并且想要在列表展示，就可以使用这个配置
    # fk_fields = ('',)
    def get_queryset(self, request):
        """重写列表展示的方法"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

        # 设置软删除，删除时不删除数据，而是给原本空的删除字段值修改为删除操作执行的时间

    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        """
        obj.is_return = True
        obj.return_time = datetime.datetime.now()
        obj.save()

    def delete_queryset(self, request, queryset):
        """Given a queryset, delete it from the database."""

        for i in queryset:
            self.delete_model(request, i)

    # 一刷新list，就走这个方法
    def changelist_view(self, request, extra_context=None):
        user = request.user
        if not user.is_superuser:
            self.readonly_fields = ['is_return', 'is_overdue']
            self.fields = ('book',)
        else:
            pass
        return super(BorrowAdmin, self).changelist_view(request, extra_context=None)

    def save_model(self, request, obj, form, change):
        """Given a model instance save it to the database."""
        if not change:
            if not request.user.is_superuser:
                obj.user = request.user

        super(BorrowAdmin, self).save_model(request, obj, form, change)


admin.site.register(Borrow, BorrowAdmin)

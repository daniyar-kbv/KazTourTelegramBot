from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from main.models import TelegramUser, QuestionAnswer, SurveyQuestion, BotText, ContactType, UserData, BotMode
from main.forms import QuestionAnswerForm, SurveyQuestionForm, BotTextForm


class QuestionAnswerInline(SortableInlineAdminMixin, admin.TabularInline):
    model = QuestionAnswer
    form = QuestionAnswerForm
    extra = 0


@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = SurveyQuestionForm
    inlines = [QuestionAnswerInline]


@admin.register(BotText)
class BotTextAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ['id']
    form = BotTextForm

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ContactType)
class ContactTypeAdmin(admin.ModelAdmin):
    pass


class UserDataInline(admin.StackedInline):
    model = UserData
    readonly_fields = ['contact_type', 'answers', 'audio_suggestion', 'start_date', 'end_date']
    extra = 0


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name']
    search_fields = ['username', 'first_name', 'last_name', 'phone_number']
    readonly_fields = ['id', 'username', 'first_name', 'last_name', 'phone_number', 'current_step', 'current_sub_step',
                       'current_micro_step']
    inlines = [UserDataInline]

# Uncomment if multiple modes exist
# @admin.register(BotMode)
# class BotModeAdmin(admin.ModelAdmin):
#     list_display = ['type', 'is_enabled']
#     readonly_fields = ['type']
#
#     def has_add_permission(self, request):
#         return False
#
#     def has_delete_permission(self, request, obj=None):
#         return False


admin.site.site_header = 'Администрирование Kaztour Telegram Bot'
admin.site.site_title = 'Сайт Администрирования Kaztour Telegram Bot'
admin.site.index_title = index_title = 'Kaztour Telegram Bot'
admin.site.site_url = None

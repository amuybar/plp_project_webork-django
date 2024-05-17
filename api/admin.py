from django import forms
from django.contrib import admin
from django.core.mail import send_mail

from .models import BidService, GetStarted, Messages, Newsletter, Services

admin.site.register(BidService)
admin.site.register(GetStarted)
admin.site.register(Messages)
admin.site.register(Services)

class NewsletterAdminForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Newsletter
        fields = '__all__'

class NewsletterAdmin(admin.ModelAdmin):
    form = NewsletterAdminForm
    list_display = ('email',)
    actions = ['send_newsletter']

    def send_newsletter(self, request, queryset):
        message = request.POST.get('message') 
        recipients = [subscriber.email for subscriber in queryset] 
        send_mail(
            'Webworks Labs ',
            message,
            'webworks@labs.mail',
            recipients,
            fail_silently=False,
        )

    send_newsletter.short_description = "Send newsletter to selected subscribers"

admin.site.register(Newsletter, NewsletterAdmin)
from django.contrib import admin
from .models import recruitments
from django.core.mail import send_mail, EmailMessage
from django.core import mail
from django.template.loader import render_to_string
import threading
from threading import Thread
from django.conf import settings
from import_export.admin import ImportExportModelAdmin

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMessage(self.subject, self.html_content, settings.EMAIL_HOST_USER, bcc=self.recipient_list)
        msg.content_subtype = "html"
        msg.send()

def send_html_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()


class recruitmentsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = recruitments
    fields = ['name', 'email_personal', 'email_kiet', 'library_id', 'contact_no',
              'day_scholar_hosteller', 'gender', 'branch', 'payment_mode', 'desk', 'date', 'payment_status', 'recruitment_mail']

    list_display = ('name', 'payment_status', 'recruitment_mail','email_kiet', 'contact_no', 'id')

    list_per_page = 65

    list_filter = ('gender', 'day_scholar_hosteller', 'desk', 'payment_mode' ,'payment_status', 'date', 'recruitment_mail')

    search_fields = ('email_personal', 'email_kiet',
                     'name', 'contact_no', 'library_id')

    ordering = ('name', 'id')

    actions = ["send_confirmation_mail",
                "send_test_slot_mail",

                "send_day4_slot1_lab1_mail_adv",
                "send_day4_slot1_lab2_mail_adv",
                "send_day4_slot1_lab3_mail", 
                "send_day4_slot1_lab4_mail",

                "send_day4_slot2_lab1_mail", 
                "send_day4_slot2_lab2_mail", 
                "send_day4_slot2_lab3_mail", 
                "send_day4_slot2_lab4_mail", ]
   

    # def send_confirmation_mail(self, request, queryset):
    #     connection = mail.get_connection()
    #     pl =[]
    #     for i in queryset:
    #         if i.email_personal:
    #             pl.append(i.email_personal)
    #         # else:

    #     connection.open()
    #     message= render_to_string('confirmation.html')
    #     send_html_mail('Innogeeks Recruitment | Registration Successful',message,pl)

    #     connection.close()
    #     queryset.update(payment_status=True)
    # send_confirmation_mail.short_description = "Send a payment confirmation mail"

    # def send_test_slot_mail(self, request, queryset):
    #     connection = mail.get_connection()
    #     for i in queryset:
    #         if i.email_personal:
    #             connection.open()
    #             message= render_to_string('test_slot.html',{"id":i.id, "name": i.name})
    #             send_html_mail('Innogeeks Recruitment | Test IDs and Slots',message, [i.email_personal])
    #             connection.close()
    #             queryset.update(recruitment_mail=True)
    # send_test_slot_mail.short_description = "Send test slot mail"

    
    # ##########################################     DAY 4-----SLOT 1        ##################################

    def send_day4_slot1_lab1_mail_adv(self, request, queryset):
        connection = mail.get_connection()
        for i in queryset:
            if i.email_personal:
                connection.open()
                message= render_to_string('day4_slot1_lab1.html',{"id":i.id+100, "name": i.name})
                send_html_mail('Innogeeks Recruitment | Test IDs and Slots',message, [i.email_personal])
                connection.close()
                queryset.update(recruitment_mail=True)
    send_day4_slot1_lab1_mail_adv.short_description = "DAY-1 SLOT-1 LAB-1"

    def send_day4_slot1_lab2_mail_adv(self, request, queryset):
        connection = mail.get_connection()
        for i in queryset:
            if i.email_personal:
                connection.open()
                message= render_to_string('day4_slot1_lab2.html',{"id":i.id+100, "name": i.name})
                send_html_mail('Innogeeks Recruitment | Test IDs and Slots',message, [i.email_personal])
                connection.close()
                queryset.update(recruitment_mail=True)
    send_day4_slot1_lab2_mail_adv.short_description = "DAY-1 SLOT-1 LAB-2"

    def send_day4_slot1_lab3_mail(self, request, queryset):
        connection = mail.get_connection()
        for i in queryset:
            if i.email_personal:
                connection.open()
                message= render_to_string('day4_slot1_lab3.html',{"id":i.id, "name": i.name})
                send_html_mail('Innogeeks Recruitment | Test IDs and Slots',message, [i.email_personal])
                connection.close()
                queryset.update(recruitment_mail=True)
    send_day4_slot1_lab3_mail.short_description = "DAY-1 SLOT-1 LAB-3"

    # def send_day4_slot1_lab4_mail(self, request, queryset):
    #     connection = mail.get_connection()
    #     for i in queryset:
    #         if i.email_personal:
    #             connection.open()
    #             message= render_to_string('day4_slot1_lab4.html',{"id":i.id, "name": i.name})
    #             send_html_mail('Innogeeks Recruitment | Test IDs and Slots',message, [i.email_personal])
    #             connection.close()
    #             queryset.update(recruitment_mail=True)
    # send_day4_slot1_lab4_mail.short_description = "DAY-4 SLOT-1 LAB-4"


    # ##########################################     DAY 4-----SLOT 2        ##################################
    def send_day4_slot2_lab1_mail(self, request, queryset):
        connection = mail.get_connection()
        for i in queryset:
            if i.email_personal:
                connection.open()
                message= render_to_string('day4_slot2_lab1.html',{"id":i.id, "name": i.name})
                send_html_mail('Innogeeks Recruitment | Test IDs and Slots',message, [i.email_personal])
                connection.close()
                queryset.update(recruitment_mail=True)
    send_day4_slot2_lab1_mail.short_description = "DAY-1 SLOT-2 LAB-1"

    def send_day4_slot2_lab2_mail(self, request, queryset):
        connection = mail.get_connection()
        for i in queryset:
            if i.email_personal:
                connection.open()
                message= render_to_string('day4_slot2_lab2.html',{"id":i.id, "name": i.name})
                send_html_mail('Innogeeks Recruitment | Test IDs and Slots',message, [i.email_personal])
                connection.close()
                queryset.update(recruitment_mail=True)
    send_day4_slot2_lab2_mail.short_description = "DAY-1 SLOT-2 LAB-2"

    def send_day4_slot2_lab3_mail(self, request, queryset):
        connection = mail.get_connection()
        for i in queryset:
            if i.email_personal:
                connection.open()
                message= render_to_string('day4_slot2_lab3.html',{"id":i.id, "name": i.name})
                send_html_mail('Innogeeks Recruitment | Test IDs and Slots',message, [i.email_personal])
                connection.close()
                queryset.update(recruitment_mail=True)
    send_day4_slot2_lab3_mail.short_description = "DAY-1 SLOT-2 LAB-3"

    # def send_day4_slot2_lab4_mail(self, request, queryset):
    #     connection = mail.get_connection()
    #     for i in queryset:
    #         if i.email_personal:
    #             connection.open()
    #             message= render_to_string('day4_slot2_lab4.html',{"id":i.id, "name": i.name})
    #             send_html_mail('Innogeeks Recruitment | Test IDs and Slots',message, [i.email_personal])
    #             connection.close()
    #             queryset.update(recruitment_mail=True)
    # send_day4_slot2_lab4_mail.short_description = "DAY-1 SLOT-2 LAB-4"


admin.site.register(recruitments, recruitmentsAdmin)
from django.urls import path
from consults.views import *
urlpatterns=[
    path('send/',sendDconsult,name='send-consult'),
    path('my/',myConsults,name='my-consults'),
    path('set-reply/<int:id>',setConsultReply,name='set-reply-consults'),
    path('consult/<int:id>',consult,name='consult'),

]
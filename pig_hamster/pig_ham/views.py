from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

@request_mapping("")
class MyView(View):
    @request_mapping("/", method="get")
    def home(self, request):
        return render(request, 'PigHamster/pig_hamster/templates/contact')

    @request_mapping("/member_info", method="get")
    def mInfo(self, request):
        return render(request, 'PigHamster/pig_hamster/templates/member_info.html')

    @request_mapping("/contact", method="get")
    def contact(self, request):
        return render(request, 'PigHamster/pig_hamster/templates/contact.html')

    @request_mapping("/join", method="get")
    def join(self, request):
        return render(request, 'PigHamster/pig_hamster/templates/join_us_condition.html')



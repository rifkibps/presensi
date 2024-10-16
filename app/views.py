from django.shortcuts import render
from django.views import View
from . import models

# Create your views here.
class DashboardAppClassView(View):

    def get(self, request):

        context = {
            'title' : 'Hello World'
        }

        return render(request, 'app/index.html', context)


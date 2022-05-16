from django.views.generic import ( ListView,
                                   CreateView,
                                   UpdateView,
                                   DeleteView,
                                   TemplateView,
                                   DetailView,
                                   View
                                    )

from django.views import render 
from .models import Snack



class HomeView(TemplateView):
    template_name = "home.html"
    

class SnacksListView(ListView):
    template_name = "snack_list.html"
    model = Snack

class SnacksDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack


class SnacksCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["title", "purchaser","description"]



class SnacksUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["name", "rating"]

class ThingsDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url ='/'


class MyCustomView(View):

    queryset= Snack.objects.all
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        data = request.data

        my_snack={
            "title" : data["title"],
            "purchaser" : data["purchaser"],

      

        }

        my_object = Snack.objects.create(**my_snack)
        my_object.save()

        return render(request, "home.html", {})




    def put(self, request, *args, **kwargs):
        pass


    def delete(self, request, *args, **kwargs):
        pass
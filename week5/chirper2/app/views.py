from django.shortcuts import render

from app.models import Chirp

# Create your views here.
def index_view(request):
    print(request.POST)
    if request.POST:
        chirp_body = request.POST["chirp_body"]
        if chirp_body != "" and len(chirp_body) <= 140:
            Chirp.objects.create(body=chirp_body)
    context = {
        "all_chirps": Chirp.objects.all().order_by("-created")
    }
    return render(request, "index.html", context)

def about_view(request):
    print("JOEL!!!!!" * 40)
    message = request.POST.get("message", "")
    voice = request.POST.get("voice", "")
    print(message, voice)
    print(request.POST)
    return render(request, "about.html")

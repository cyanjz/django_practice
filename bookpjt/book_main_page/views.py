from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')
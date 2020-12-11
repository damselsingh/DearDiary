from django.shortcuts import render, redirect
from .models import Diary
from .forms import DiaryForm

# Create your views here.
def home(request):
    diaries = Diary.objects.order_by('-id')[:4]
    forms = DiaryForm()
    if request.method == 'POST':
        forms = DiaryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    context = {'diaries': diaries, 'forms': forms}
    return render(request, 'diary/index.html', context)

def update_diary(request, pk):
    diaries = Diary.objects.get(id=pk)
    forms = DiaryForm(instance=diaries)
    if request.method == 'POST':
        forms = DiaryForm(request.POST, instance=diaries)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    context = {'forms': forms}
    return render(request, 'diary/updatediary.html', context)

def delete_diary(request, pk):
    diaries = Diary.objects.get(id=pk)
    diaries.delete()
    return redirect('/')

def see(request):
    diaries = Diary.objects.order_by('-id')
    return render(request, 'diary/seeall.html', {'diaries': diaries})
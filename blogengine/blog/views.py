from django.shortcuts import render

# Create your views here.
def posts_list(request):
    names = ['john', 'jane', 'bob', 'bill']
    return render(request, 'blog/index.html', context={'names': names})
from django.shortcuts import render

posts = [
    {
        'author':'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author':'Joinal',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 20, 2024'
    },
    
]

def home(request):
    context = {
        'posts':posts
    }
    
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})

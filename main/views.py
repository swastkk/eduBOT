from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bookbuddy.models import Bookbuddy
from youtubeplus.models import Youtubeplus
from learnit.models import Learnit
# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'enterpage.html')
    else:
        # do something for authenticated users
        return render(request, 'home.html')


@login_required
def profile(request):
    user = request.user
    bookbuddy = Bookbuddy.objects.filter(user=user)
    youtubeplus = Youtubeplus.objects.filter(user=user)
    learnit = Learnit.objects.filter(user=user)
    context = {
        'user': user,
        'bookbuddy': bookbuddy,
        'youtubeplus': youtubeplus,
        'learnit': learnit
    }
    return render(request, 'account/profile.html', context)


from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

def pharma_login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.user_type == 'patient':
            return HttpResponseRedirect(reverse('pharma_login'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view
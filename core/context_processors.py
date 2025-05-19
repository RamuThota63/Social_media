from .models import FriendRequest
from core.models import Post

def friend_request_count(request):
    if request.user.is_authenticated:
        count = FriendRequest.objects.filter(to_user=request.user).count()
    else:
        count = 0
    return {'friend_request_count': count}
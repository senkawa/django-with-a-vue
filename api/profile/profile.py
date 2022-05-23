from django.contrib.auth import authenticate, login as authlogin
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.http import JsonResponse, HttpRequest

from api.models import User


def index(request: HttpRequest):
    if request.user.is_authenticated:
        user: User = request.user
        user.note_set.create(description="XDDD")

        aaa = User.objects.prefetch_related("note_set").all()

        return JsonResponse({"data": list(aaa[0].note_set.values())}, safe=False)
    else:
        return JsonResponse({"msg": "unauthenticated"})


def login(request: HttpRequest):
    if request.method == "POST":
        user: User = authenticate(username=request.POST["username"], password=request.POST["password"])  # type: ignore
        if user is not None:
            authlogin(request, user)
            return JsonResponse({"email": user.email})
        else:
            return JsonResponse({"err": "failed"})

    return JsonResponse({"xd": 123})


@login_required
def me(request: HttpRequest):
    return JsonResponse(
        model_to_dict(
            request.user,
            fields=[
                "id",
                "username",
                "email",
            ],
        )
    )

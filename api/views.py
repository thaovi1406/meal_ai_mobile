from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_api(request):
    if request.method != "POST":
        return JsonResponse(
            {"message": "Login API OK - use POST"},
            status=405
        )

    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        return JsonResponse({
            "status": "success",
            "message": "Login success",
            "username": user.username
        })
    else:
        return JsonResponse({
            "status": "fail",
            "message": "Sai tài khoản hoặc mật khẩu"
        }, status=401)

def user_info(request):
    if request.user.is_authenticated:
        return {"papel": request.user.papel}
    return {}

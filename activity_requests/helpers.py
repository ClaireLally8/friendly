from .models import Request


def update_remaining_requests(id, value):
    Request.objects.filter(request_activity=id).update(accepted=value)

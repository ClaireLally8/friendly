from .models import Request

def update_remaining_requests(id, value):
    # Get the requests linked to activity
    # Loop through requests
    # Set the value to whats stated in the call
    reqs = Request.objects.filter(request_activity=id, accepted=value).values()
    for req in reqs:
        req.accepted = value
        req.save()


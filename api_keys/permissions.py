__author__ = 'taylor'

__author__ = 'Taylor'

from rest_framework.permissions import BasePermission

from .models import Client


class AuthorizedClientPermission(BasePermission):

    def has_permission(self, request, view):
        try:
            api_key = request.META['HTTP_API_KEY']
        except KeyError:
            return False
        is_authorized = Client.objects.filter(key=api_key).exists()
        return is_authorized

from django.core.exceptions import PermissionDenied


class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if hasattr(instance, 'creator'):
            if instance.creator != self.request.user:
                raise PermissionDenied
            
        elif hasattr(instance, 'author'):
            if instance.author != self.request.user:
                raise PermissionDenied
            
        return super().dispatch(request, *args, **kwargs)
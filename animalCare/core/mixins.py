from django.contrib.auth import mixins as auth_mixins


class AllowedGroups():
    def __init__(self, group):
        self.group = group

    def dispatch(self, request, *args, **kwargs):
        group = request.user.groups.all()[0].name
        if self.group == group:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

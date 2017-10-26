from rest_framework.routers import DefaultRouter


class ExtendableRouter(DefaultRouter):
    """
    Extends `DefaultRouter` class to add a method for extending url routes from another router.
    """
    def extend(self, router):
        """
        Extend the routes with url routes of the passed in router.
        """
        self.registry.extend(router.registry)

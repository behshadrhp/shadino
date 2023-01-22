from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet


class CreateRetrieveDestroyGenericViewSet(CreateModelMixin,
                                          RetrieveModelMixin,
                                          DestroyModelMixin,
                                          GenericViewSet):
    """
        A viewset that provides `retrieve` and `create` and `Destroy` actions.
    """
    pass

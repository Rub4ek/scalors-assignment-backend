class NestedViewSetMixin(object):
    parent = None
    parent_lookup_field = 'nested'

    def get_nested_filter_dict(self):
        filter_dict = {}
        if not self.parent:
            return filter_dict
        viewset = self.parent(request=self.request)
        if isinstance(viewset, NestedViewSetMixin):
            filter_dict.update(viewset.get_nested_filter_dict())
        filter_dict.update({self.parent_lookup_field:
                            self.kwargs.get('%s_%s' % (self.parent_lookup_field, viewset.lookup_field))})
        return filter_dict

    def get_queryset(self):
        return super(NestedViewSetMixin, self).get_queryset().filter(**self.get_nested_filter_dict())

    def perform_create(self, serializer):
        viewset = self.parent(
            request=self.request,
            kwargs={self.parent.lookup_field:
                    self.get_nested_filter_dict().get(self.parent_lookup_field)})
        serializer.save(**{self.parent_lookup_field: viewset.get_object()})

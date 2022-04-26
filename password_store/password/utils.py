from password.models import *

class DataMixim:
    # paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        if context.get('cats', False) != False:
            cats = Category.objects.all().values('id', 'name_category', 'parent_id')
            context['cats'] = cats

        return context
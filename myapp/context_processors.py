# As we are using context processor we have to register in project's setting file in templates as 'category.context_processors'

from .models import Category


def menu_links(request):
    # next line gives, all the category
    links = Category.objects.all()

    # next line does, all the category will be stored in 'links' varaible and we can use it when we want
    return dict(links=links)
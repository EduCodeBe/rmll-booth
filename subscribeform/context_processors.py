from juri import settings


def add_templates_vars(request):
    print settings.BASE_TEMPLATE
    return {
        'BASE_TEMPLATE': settings.BASE_TEMPLATE[request.LANGUAGE_CODE],
        'LANGUAGE_LINKS': settings.LANGUAGE_LINKS,
    }

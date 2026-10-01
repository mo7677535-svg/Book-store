from .models import SiteSettings

def settings_context(request):
    settings = SiteSettings.objects.first()
    return {'site_settings': settings}
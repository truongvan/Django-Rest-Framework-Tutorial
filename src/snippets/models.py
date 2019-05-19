from django.db import models
from django.utils.translation import ugettext_lazy as _
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGES_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(_("Create"), auto_now=False, auto_now_add=True)
    title = models.CharField(_("Title"), max_length=100, blank=True, default='')
    code = models.TextField(_("Code"))
    lineos = models.BooleanField(_("Lineos"), default=False)
    language = models.CharField(_("Language"), max_length=100, choices=LANGUAGES_CHOICES, default='python')
    style = models.CharField(_("Style"), max_length=100, choices=STYLE_CHOICES, default='friendly')

    class Meta:
        ordering = ("created", )
from rest_framework.parsers import JSONParser
import ujson
from django.conf import settings
from django.utils import six


class UJSONParser(JSONParser):

    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        try:
            data = stream.read().decode(encoding)
            return ujson.loads(data)
        except ValueError as e:
            raise ParseError('JSON parse error - %s' % six.text_type(exc))

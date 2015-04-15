#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
    copy from scrapy.utils.url.py
"""
import urlparse
import urllib

_ALWAYS_SAFE_BYTES = (b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                      b'abcdefghijklmnopqrstuvwxyz'
                      b'0123456789' b'_.-')
_reserved = b';/?:@&=+$|,#' # RFC 3986 (Generic Syntax)
_unreserved_marks = b"-_.!~*'()" # RFC 3986 sec 2.3
_safe_chars = _ALWAYS_SAFE_BYTES + b'%' + _reserved + _unreserved_marks

def canonicalize_url(url, keep_blank_values=True, keep_fragments=False, encoding=None):
    scheme, netloc, path, params, query, fragment = urlparse.urlparse(unicode_to_str(url, encoding))
    keyvals = urlparse.parse_qsl(query, keep_blank_values, 0)
    keyvals.sort()
    query = urllib.urlencode(keyvals)

    for reserved in ('2f', '2F', '3f', '3F'):
        path = path.replace('%' + reserved, '%25' + reserved.upper())
    path = urllib.unquote(path)
    path = safe_url_string(path) or '/'

    fragment = '' if not keep_fragments else fragment
    return urlparse.urlunparse((scheme, netloc.lower(), path, params, query, fragment))


def unicode_to_str(text, encoding=None, errors='strict'):
    if encoding is None:
        encoding = 'utf-8'
    if isinstance(text, unicode):
        return text.encode(encoding, errors)
    elif isinstance(text, str):
        return text
    else:
        raise TypeError('unicode_to_str must receive a unicode or str object, got %s' % type(text).__name__)

def safe_url_string(url, encoding='utf8'):
    s = unicode_to_str(url, encoding)
    return urllib.quote(s, _safe_chars)



def test():
    pass

if __name__ == "__main__":
    test()


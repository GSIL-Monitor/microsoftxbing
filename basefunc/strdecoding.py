# -*- coding: utf-8 -*-
import chardet


class Decode4Str:

    @staticmethod
    def decodestr(string,decode='utf-8'):
        if not isinstance(string, unicode):
            string = unicode(string, decode)
        srcencode = chardet.detect(string)['encoding']
        if srcencode in ['ascii']:
            cont = unicode(string,encoding=decode)
        elif srcencode in ['utf-8', 'utf8']:
            cont = string
        else:
            print srcencode
            cont = string.encode(srcencode).decode(decode)
        return cont, srcencode

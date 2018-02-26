# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 22:17:06 2017

@author: 69568
"""

import re
query='~H(Joe)'
if re.match(r'(^[\~])', query):
    print 'yes'
#    query=re.sub('~','',query)
    query=query[1:]
print query
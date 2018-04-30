# coding: utf8
from __future__ import unicode_literals, print_function, division

from pyconcepticon import api
from clldutils.misc import lazyproperty

from pylexibank.util import Repos


class Concepticon(api.Concepticon, Repos):
    @lazyproperty
    def cached_glosses(self):
        return {int(cs.id): cs.gloss for cs in self.conceptsets.values()}

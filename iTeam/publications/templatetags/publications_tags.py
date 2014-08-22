#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Adrien Chardon
# @Date:   2014-08-19 17:04:25
# @Last Modified by:   Adrien Chardon
# @Last Modified time: 2014-08-22 17:14:48

# This file is part of iTeam.org.
# Copyright (C) 2014 Adrien Chardon (Nodraak).
#
# iTeam.org is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# iTeam.org is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with iTeam.org. If not, see <http://www.gnu.org/licenses/>.


import markdown

from django import template
from django.utils.safestring import mark_safe

from iTeam.member.models import Profile

register = template.Library()


@register.filter
def iteam_markdown(value):
    html = markdown.markdown(value, safe_mode='escape', extensions=['codehilite(linenums=True)', 'extra'])
    return mark_safe(html)

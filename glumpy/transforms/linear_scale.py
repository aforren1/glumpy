#! /usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
from . import Transform


class LinearScale(Transform):

    # uniform vec3 scale
    shaderfile = "linear-scale-forward.glsl"


    def __init__(self, *args, **kwargs):
        Transform.__init__(self, *args, **kwargs)


    @property
    def scale(self):
        return self['scale']

    @scale.setter
    def scale(self, value):
        self['scale'] = value

#!/usr/bin/env python
# coding: utf-8

from django import forms as dforms
from django.forms import fields

class UserForm(dforms.Form):
    # 生成input
    username = fields.CharField()
    email = fields.EmailField()

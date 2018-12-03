#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Invoke tasks for building docops-bot documentation."""

from invocations.docs import docs, watch_docs
from invoke import Collection

ns = Collection(docs, watch_docs)
ns.configure({
    'sphinx': {
        'source': 'sites/docs',
        'target': 'sites/docs/_build',
        'target_file': 'index.html',
    },
})

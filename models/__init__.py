#!/usr/bin/python3
"""Initializes the variable storage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

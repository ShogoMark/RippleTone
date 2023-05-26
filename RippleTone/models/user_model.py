#!/usr/bin/python3

from flask import Flask, render_template, request, redirect

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences = {}
        self.history = []

    def add_preference(self, item_id, rating):
        self.preferences[item_id] = rating

    def add_to_history(self, item_id):
        self.history.append(item_id)


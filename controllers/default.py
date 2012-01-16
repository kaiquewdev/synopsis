# -*- coding: utf-8 -*-

def index():
	return {}

def about():
	return {}
	
def user():
    return {'form': auth()}

def download():
    return response.download(request,db)

def call():
    return service()

@auth.requires_signature()
def data():
    return dict(form=crud())

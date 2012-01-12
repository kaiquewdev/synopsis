# -*- coding: utf-8 -*-
import functions as f # shorthand function

@auth.requires_membership('admin')
def index(): # Show the all content for redirect to profile
	subject = f.get_table(db, 'subject', order='created_on')
	return { 'subject': subject }

def profile(): # Show the profile of subject
	args = request.args
	if args: profile = f.get_table(db, 'subject', id=args[0])
	return {'profile': profile}

def new(): # Create a new subject
	return {}

def edit(): # Edit the subject
	return {}

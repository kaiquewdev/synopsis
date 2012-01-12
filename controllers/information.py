# -*- coding: utf-8 -*-
import functions as f # shorthand function

@auth.requires_membership('admin')
def index(): # Show the all content for redirect to profile
	subject = f.get_table(db, 'subject', order='created_on')
	return { 'subject': subject }

def profile(): # Show the profile of subject
	args = request.args # query url's
	if args: profile = f.get_table(db, 'subject', id=args[0]) 
	if not args or not profile: return redirect( URL('index') )
	return {'profile': profile}

def publication(): # Show the publication profile
	args = request.args # query url's
	if args: publication = f.get_table(db, 'publication', id=args[0]) 
	if not args or not publication: return redirect( URL('profile') )
	return {'publication': publication}

def new(): # Create a new subject
	return {}

def edit(): # Edit the subject
	return {}

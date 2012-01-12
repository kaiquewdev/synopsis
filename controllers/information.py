# -*- coding: utf-8 -*-
import functions as f # shorthand function

@auth.requires_membership('admin')
def index(): # Show the all content for redirect to profile
	subject = f.get_table(db, 'subject', order='created_on')
	return { 'subject': subject }

@auth.requires_membership('admin')
def profile(): # Show the profile of subject
	args = request.args # query url's
	if args: 
		profile = f.get_table(db, 'subject', id=args[0]) 
		session.index = args[0] 
	if not args or not profile: return redirect( URL('index') )
	return { 'profile': profile }

@auth.requires_membership('admin')
def publication(): # Show the publication profile
	args = request.args # query url's
	count_equals = f.count_equals
	if args: 
		publication = f.get_table(db, 'publication', id=args[0])
		session.back = args[0] 
	if not args or not publication: return redirect( URL('profile') )
	return { 'publication': publication, 
			 'count_equals': count_equals }

@auth.requires_membership('admin')
def new(): # Create a new subject
	args = request.args
	
	if not args:
		title = 'Subject'
		subject = SQLFORM(db.subject, fields=['name'])
		subject.elements(_type='submit')[0]['_value'] = 'Create'
		
		if subject.process().accepted:
			response.flash = T('{0} {1} {2}'.format('New', title.lower(), 'inserted!'))
		elif subject.errors:
			response.flash = T('Sorry, try again!')
		else:
			response.flah = T('Please, fill the field...')
			
		return { 'form': subject, 
			 	 'title': title }
	
	elif args[0] == 'publication':
		title = 'Publication'
		publication = SQLFORM(db.publication, fields=['title', 'sub_title'])
		publication.vars.subject_id = args[1]
		if publication.process().accepted:
			response.flash = T(T('{0} {1} {2}'.format('New', title.lower(), 'inserted!')))
		elif publication.errors:
			response.flash = T('Sorry, try again!')
		else:
			response.flahs = T('Please, fill the field...')
	
		return { 'form': publication,
				 'title': title }
	elif args[0] == 'column':
		title = 'Topic'
		column = SQLFORM(db.column, fields=['title'])
		column.vars.publication_id = args[1]
		if column.process().accepted:
			response.flash = T(T('{0} {1} {2}'.format('New', title.lower(), 'inserted!')))
		elif column.errors:
			response.flash = T('Sorry, try again!')
		else:
			response.flahs = T('Please, fill the field...')
	
		return { 'form': column,
				 'title': title }
	elif args[0] == 'row':
		title = 'Row for {0}'.format(db.column(args[1])['title'])
		row = SQLFORM(db.row, fields=['content'])
		row.vars.column_id = args[1]
		if row.process().accepted:
			response.flash = T(T('{0} {1} {2}'.format('New', title.lower(), 'inserted!')))
		elif row.errors:
			response.flash = T('Sorry, try again!')
		else:
			response.flahs = T('Please, fill the field...')
	
		return { 'form': row,
				 'title': title }
			 	 
@auth.requires_membership('admin')
def edit(): # Edit the subject
	return {}

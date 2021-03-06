# -*- coding: utf-8 -*-
import functions as f # shorthand function

@auth.requires_login()
def index(): # Show the all content for redirect to profile
	subject = f.get_table(db, 'subject', order='created_on')
	return { 'subject': subject }

@auth.requires_login()
def profile(): # Show the profile of subject
	args = request.args # query url's
	if args: 
		profile = f.get_table(db, 'subject', id=args[0]) 
		session.index = args[0] 
	if not args or not profile: return redirect( URL('index') )
	return { 'profile': profile }

@auth.requires_login()
def publication(): # Show the publication profile
	args = request.args # query url's
	count_equals = f.count_equals
	if args: 
		publication = f.get_table(db, 'publication', id=args[0])
		session.back = args[0] 
	if not args or not publication: return redirect( URL('profile') )
	return { 'publication': publication, 
			 'count_equals': count_equals }

@auth.requires_login()
def new(): # Create a new subject
	args = request.args
	
	if not args: # New Subject
		title = 'Subject'
		subject = SQLFORM(db.subject, fields=['name'])
		subject.elements(_type='submit')[0]['_value'] = 'Create'
		
		if subject.process().accepted:
			response.flash = T(
                                    '{0} {1} {2}'
                                    .format('New', title.lower(), 'inserted!')
                                )
		elif subject.errors:
			response.flash = T('Sorry, try again!')
		else:
			response.flah = T('Please, fill the field...')
			
		return { 'form': subject, 
			 	 'title': title }
	
	elif args[0] == 'publication': # New publication
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
				 
	elif args[0] == 'quote': # New quote
		title = 'Quote'
		quote = SQLFORM(db.quote, fields=['content'])
		quote.vars.publication_id = args[1]
		if quote.process().accepted:
			response.flash = T(T('{0} {1} {2}'.format('New', title.lower(), 'inserted!')))
		elif quote.errors:
			response.flash = T('Sorry, try again!')
		else:
			response.flahs = T('Please, fill the field...')
	
		return { 'form': quote,
				 'title': title }
				 
	elif args[0] == 'column': # New column
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
	
	elif args[0] == 'line': # New line
		title = 'Line'
		line = FORM()
		
		for publication in f.get_table(db, 'publication', id= args[1]):
			for column in publication.column.select():					
				line.append(LABEL('{0}{1}'.format(column.title, ':')))
				line.append(BR())
				line.append(INPUT(_name=column.id, _type='text', requires=[IS_NOT_EMPTY()]))
				line.append(BR())
		
		line.append(INPUT(_type='submit', _value=T('Create')))
		
		if line.process(formname='new_line').accepted:
			fields = []
			for l in line.vars:
				fields.append({'content': line.vars[l], 'column_id': l})
				
			if db.row.bulk_insert(fields):
				response.flash = T('New line was created!')
		elif line.errors:
			response.flash = T('Try the fill inputs again!')
		else:
			response.flash = T('Please, fill all inputs...')
					
		return { 'form': line,
				 'title': title }
				 
	elif args[0] == 'row': # New row (Remove this part)
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
			 	 
@auth.requires_login()
def edit(): # Edit the subject
	return {}

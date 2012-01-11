# -*- coding: utf-8 -*-

def get_publications( db, id = 0, order = '' ):
	# Get all publications or publication by id, with order or not
	
	query = db().select( db.publication.ALL )
	
	if id:
		return db(db.publication.id == id).select()
	elif order:
		return db().select(db.publication.ALL, orderby = order)
	elif id and order:
		return db(db.publication.id == id).select(orderby = order)
	else:
		return query

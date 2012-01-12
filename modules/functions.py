# -*- coding: utf-8 -*-

def get_table( db= '', tablename= '', id= 0, order= '', count= False ):
	# Get all subjects or subjects by id, with order or not
	try:
		if tablename: 
			table = db.get(tablename)
			query = db().select( table.ALL )
			
			if id:
				return db(table.id == id).select()
			elif order:
				return db().select(table.ALL, orderby = order)
			elif count:
				return db(table).count()
			elif id and order:
				return db(tablename.id == id).select(orderby = order)
			else:
				return query
		else:
			return {}
	except Exception:
		return {}
	
def count_equals(*args):
	import pdb; pdb.set_trace()
	r = []
	for i in args:
		if type(i) == list:
			for j in i:
				if not j in r:
					r.append(j)
		else:
			if not i in r:
				r.append(i)
	return len(r)

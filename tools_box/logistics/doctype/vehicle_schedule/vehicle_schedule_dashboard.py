from frappe import _

def get_data():
	return {
		'fieldname': 'vehicle_schedule',
		'transactions': [
			{
				'label': _('Transactions'),
				'items': ['Purchase Order']
			},
		]
	}
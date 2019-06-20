from flask_wtf import FlaskForm #python to HTML display
from wtforms import StringField, FormField, IntegerField, SubmitField, FieldList #importing fields
from wtforms.validators import Length, Optional, NoneOf, NumberRange, InputRequired #validations for inputs

class SearchForm(FlaskForm):
	# search params:
	# parkCode: A comma delimited list of park codes (each 4-10 characters in length)
	# stateCode: A comma delimited list of 2 character state codes
	# limit: Number of results to return per request. Default is 50
	# start: Get the next [limit] results starting with this number
	# q: Term to search on
	# fields: A comma delimited list of resource properties to include in the JSON response in addition to the default properties. The available properties for each resource are listed in the documentation for each resource. Invalid property values will be ignored.
	# sort: A comma delimited list of resource properties to sort the results by. Each resource identifies which properties are 'sortable'. Ascending order is assumed for each property. If descending order is desired, the unary negative should prefix the property name. The sortable properties are listed in the documentation for each resource. Invalid property values will be ignored
	# field format: [name] = [XField]('[tag name]', validators=[...])

	parkCode = StringField('Park Code(s)', validators=[Length(min=4, max=10, message='Park codes can only be between %(min)d and %(max)d characters long.')], description="Codes specific to each park; each code must be between 4 and 10 characters long, separated by commas.")

	stateCode = StringField('State Code(s)', validators=[InputRequired(message="You must input a 2-letter state code (see star for details)"), Length(min=2, max=2, message='State codes can only be %(min)d characters.')], description="2-letter codes IDing each US State; each 2-character code must be separated with commas.")

	limit = IntegerField('Results Limit', validators=[NumberRange(min=1, message='Negative inputs are not allowed')], description="The number of results to which you'd like to limit your search; the default is 50.", default=50)

	start = IntegerField('Start Position', validators=[NumberRange(0, message="Start value must be above 0")], description="Each search instance starts at the first result by default.", default=0)

	q = StringField('Search Type', validators=[Optional(strip_whitespace=True), NoneOf(values=',', message='More than one input is not allowed')], description="Term on which to search; e.g. 'National Park', 'National Monument', etc...")

	fields = StringField('Fields', validators=[Optional(strip_whitespace=True)], description="List of search parameters separated by commas.")
	sort = StringField('Sort By', description="Designated parameter(s) by which to sort the results.")

	submit = SubmitField('Search')

class SearchTypeForm(FlaskForm):
	selection = IntegerField('Search For', validators=[NumberRange(1, 10)], description="Select your type of search out of the available options.")
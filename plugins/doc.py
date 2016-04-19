from oletools import olevba

class Plugin:

	__NAME__ = 'doc'

	def __init__(self, args):
		self.args = args
		self.analyzed_mimes = ['application/msword',
								'application/vnd.ms-office']

	def analyze(self, afile):
		
		if afile.mime_type in self.analyzed_mimes:
			parser = olevba.VBA_Parser(afile.path)
			results = parser.analyze_macros()

			if results is not None:
				for kw_type, keyword, description in results:
					output = 'type: %s keyword: %s description: %s\n' % (kw_type, keyword, description)
			else:
				output = None

			afile.plugin_output[self.__NAME__] = output

			# The parser requires an explicit close
			parser.close()
from hashlib import sha256

class Plugin:

	__NAME__ = 'sha256'

	def __init__(self, args):

		self.chunk_size = args.get('chunk_size')
		if self.chunk_size == None:
			self.chunk_size = 4096

	def analyze(self, afile):

		hasher = sha256()
		with open(afile.path, 'rb') as f:
			for chunk in iter(lambda: f.read(self.chunk_size), b""):
				hasher.update(chunk)

			afile.sha256 = hasher.hexdigest()
			afile.plugin_output[self.__NAME__] = afile.sha256
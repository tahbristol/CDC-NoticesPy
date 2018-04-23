from setuptools import setup

setup(
	name='CdcNotices',
	version='1.0',
	py_modules=['cli'],
	install_requires=[
		'Click'
	],
	entry_points='''
		[console_scripts]
		cli=cli:get_notices
		'''
)


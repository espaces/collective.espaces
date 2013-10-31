from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(name='collective.espaces',
      version=version,
      description="Policy and configuration for the eSpaces project, powered by Plone.",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone Dexterity Spaces Policy',
      author='JCU eResearch Centre',
      author_email='eresearch@jcu.edu.au',
      url='https://github.com/collective/collective.espaces',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.jbot',
          'plone.app.theming',
          'diazotheme.bootswatch',
          'plone.app.caching',
          'plone.app.theming',
          'collective.spaces',
          'collective.behavior.localanalytics',
          'collective.behavior.localdiazo',
          'collective.aaf',
          'Products.OpenXml',
          'Products.RedirectionTool',
          'Products.PloneFormGen',
          'collective.portlet.twitter',
          'collective.limitfilesizepanel',
          # -*- Extra requirements: -*-
      ],
      extras_require={'test': ['ipdb',
                               'collective.spaces[test]',
                               'collective.aaf[test]',
                               'plone.app.testing[robot]',
                               'plone.app.robotframework']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript", 'setuptools-git'],
      paster_plugins=["templer.localcommands"],
      )

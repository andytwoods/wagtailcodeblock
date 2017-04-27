from setuptools import setup, find_packages
setup(
    name='wagtailcodeblock',
    version="0.2.4",
    description='Wagtail Code Block provides PrismJS syntax highlighting in Wagtail.',
    long_description='A work-in-progress alpha of a Wagtail Streamfield block for source code with real-time syntax highlighting.',
    author='Tim Allen',
    author_email='tallen@wharton.upenn.edu',
    url='https://github.com/FlipperPA/wagtailcodeblock',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'wagtail>=1.8',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

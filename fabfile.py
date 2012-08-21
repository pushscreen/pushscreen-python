from fabric.api import local

import pushscreen


def readme():
    local('pandoc -t rst README.md > README.rst')
    local('git commit README.rst -m "Update README.rst."')

def version():
    print pushscreen.__version__

def bump(new_version):
    local('sed -i "" "s/^__version__ = .*$/__version__ = \'%s\'/g" pushscreen/__init__.py' % new_version)
    local('git commit pushscreen/__init__.py -m "Bump version to %s"' % new_version)

def release(new_version):
    if new_version != pushscreen.__version__:
        bump(new_version)
    readme()
    test()
    upload()

def upload():
    local('python setup.py sdist upload')

def test():
    local('python setup.py test')

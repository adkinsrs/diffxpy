from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

from .log_cfg import logger, unconfigure_logging, enable_logging

__author__ = ', '.join([
    'David Sebastian Fischer',
    'Florian Hölzlwimmer'
])
__email__ = ', '.join([
    'david.fischer@helmholtz-muenchen.de'
])

from . import _version
__version__ = _version.get_versions()['version']

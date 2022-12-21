from pathlib import Path
import testpub

def pytest_report_header(config):
    """Add information on the package version used in the tests.
    """
    modpath = Path(testpub.__file__).resolve().parent
    return [ "test-publish: %s" % (testpub.__version__),
             "              %s" % (modpath)]

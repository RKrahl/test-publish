from pathlib import Path
import test-publish

def pytest_report_header(config):
    """Add information on the package version used in the tests.
    """
    modpath = Path(test-publish.__file__).resolve().parent
    return [ "test-publish: %s" % (test-publish.__version__),
             "           %s" % (modpath)]

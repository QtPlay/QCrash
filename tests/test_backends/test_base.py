from qcrash.backends.base import BaseBackend
from qcrash.formatters.email import EmailFormatter


def test_qsettings():
    b = BaseBackend(None, '', '', None)
    assert b.qsettings() is not None


def test_set_formatter():
    b = BaseBackend(None, '', '', None)
    assert b.formatter is None
    b.set_formatter(EmailFormatter("test"))
    assert isinstance(b.formatter, EmailFormatter)

import sys
from core.mail import check_mailaddres

sys.path.append("../../..")


def test_check_mailaddress():
    try:
        check_mailaddres("a12345@gunma.kosen-ac.jp")
        assert True
    except ValueError as e:
        assert False

    try:
        check_mailaddres("a12345@outlook.com")
        assert True
    except ValueError as e:
        assert False

    try:
        check_mailaddres("a-123.456@gmail.com")
        assert True
    except ValueError as e:
        assert False

    try:
        check_mailaddres("a-12345")
        assert False
    except ValueError as e:
        assert True

    try:
        check_mailaddres(" a12345@outlook.com")
        assert False
    except ValueError as e:
        assert True

    assert True

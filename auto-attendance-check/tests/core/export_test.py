import sys
from core.export import ClassRegister, AttendanceState

sys.path.append("../../..")

def test_init():
    cr = ClassRegister(1)
    test_data = [{
        "student number": 1,
        "name": "",
        "attendance state": AttendanceState.ERROR.value
    }]
    assert(cr.data == test_data)


def test_export_csv():
    pass


def test_export_json():
    pass

from core.export import *

def test_init():
	cr = ClassRegister(1)
	assert(
		cr.data,
		{
			"student number": 1,
			"name": "",
			"attendance state": AttendanceState.ERROR.value
		}
	)

def test_export_csv():
	pass

def test_export_json():
	pass
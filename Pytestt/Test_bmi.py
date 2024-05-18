import Satya1.Bmi


def test_bmi_underweight():
    result = []
    input_hei = 1.72
    input_wei = 45
    
    result = Satya1.Bmi.calc(input_hei,input_wei)
    assert (result == -1 )

def test_bmi_normalweight():
    result = []
    input_hei = 1.72
    input_wei = 58
    
    result = Satya1.Bmi.calc(input_hei,input_wei)
    assert (result == 0 )

def test_bmi_overweight():
    result = []
    input_hei = 1.72
    input_wei = 80
    
    result = Satya1.Bmi.calc(input_hei,input_wei)
    assert (result == 1 )


'''def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)'''
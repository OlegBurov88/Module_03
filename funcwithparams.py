def func_with_params(a=2, b=2):
    print(a + b)


func_with_params(3, 3)

func_with_params(3)


def func_with_params2(a, b=2):
    print(a + b)


func_with_params2(3)

func_with_params2(3, 6)


def func_with_params3(a, b=2, c=5):
    print(a + b + c)


func_with_params3(3)

func_with_params3(3, 6)

func_with_params3(3, 6, 7)

func_with_params3(3, c=6)


def func_with_params(a, b=2, c=None):
    if c is None:
        c = []
        c.append(a)
    print(c)



func_with_params(3)
func_with_params(4)
func_with_params(5)
func_with_params(6)

"Print members from class inspect_me"

import inspect

import me as target_module

target_classes = set(
    [member[1] for member in inspect.getmembers(target_module, inspect.isclass)]
)
if __name__ == "__main__":
    for tg in target_classes:
        # print("target classes" % (target_classes))
        print(tg)

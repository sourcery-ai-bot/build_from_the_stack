from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *




def generate_input() -> list:
    t = gen_pos_int(10 ** 4)
    res = [t]
    for _ in range(t):
        a = gen_pos_int(10 ** 4)
        b = gen_pos_int(10 ** 4)
        x = gen_int(0, a - 1)
        y = gen_int(0, b - 1)

        res.append([a, b, x, y])

    return res


from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


te_input() -> list:
    res = []

    t = gen_pos_int(1000)
    res.append(t)

    for _ in range(t):
        a1 = gen_pos_int(10**18)
        k = gen_pos_int(10**16)
        res.append(a1)
        res.append(k)

    return 
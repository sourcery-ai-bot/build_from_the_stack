from dsl import (
    INPUT_GENERATOR,
    gen_pos_int,
    record,
    gen_int,
    to_str_then_concat_with_space,
)


INPUT_GENERATOR


def generate_input():
    t = gen_pos_int(100)
    record(t)

    for _ in range(t):
        n = gen_int(3, 100)
        record(n)

        a = [gen_pos_int(100) for _ in range(n)]
        record(to_str_then_concat_with_space(a))

        b = [gen_pos_int(100) for _ in range(n)]
        record(to_str_then_concat_with_space(b))

        c = [gen_pos_int(100) for _ in range(n)]
        record(to_str_then_concat_with_space(c))
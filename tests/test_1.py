import pytest
from src.graphs.app import to_tree


@pytest.mark.parametrize("test_input, expected", [(
        [(None, 'a'), (None, 'b'), (None, 'c')], {'a': {}, 'b': {}, 'c': {}}),
    ([
         (None, 'a'),
         (None, 'b'),
         (None, 'c'),
         ('a', 'a1'),
         ('a', 'a2'),
         ('a2', 'a21'),
         ('a2', 'a22'),
         ('b', 'b1'),
         ('b1', 'b11'),
         ('b11', 'b111'),
         ('b', 'b2'),
         ('c', 'c1'),
     ], {
         'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
         'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
         'c': {'c1': {}},
     }),
    ([(None, 'a'), ('a', 'a1'), ('a', 'a2')], {
        'a': {'a1': {}, 'a2': {}}}),
    ([(None, 'a'), ('b', 'b1'), (None, 'b')],
     {'a': {}, 'b': {'b1': {}}}),
    ([(None, 'a')], {'a': {}}),
    ([(None, 'b'), ('b', 'b1')], {'b': {'b1': {}}}),
    ([(None, 'b')], {'b': {}}),
    ([(None, 'b'), ('a', 'a1')], {'b': {}}),
])
def test_to_tree(test_input, expected):
    assert to_tree(test_input) == expected

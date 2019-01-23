import pytest
import pandas as pd

from dagger.graph import DAG


@pytest.fixture()
def simple_df1():
    return pd.DataFrame({"a": [1, 0, 1, 0, 1], "b": [1, 1, 1, 0, 0], "c": [0, 0, 1, 0, 1]})


def test_origin_nodes_1(simple_df1):
    dag = DAG(simple_df1).add_edge("a", "b").add_edge("b", "c").add_edge("a", "c")
    assert dag.origin_nodes == ("a",)


def test_origin_nodes_2(simple_df1):
    dag = DAG(simple_df1).add_edge("a", "b").add_edge("c", "b")
    assert dag.origin_nodes == ("a", "c")


def test_parent_child1(simple_df1):
    dag = DAG(simple_df1).add_edge("a", "b").add_edge("c", "b").add_edge("a", "c")
    assert set(dag.children("a")) == {"b", "c"}
    assert set(dag.children("b")) == set()
    assert set(dag.children("c")) == {"b"}
    assert set(dag.parents("a")) == set()
    assert set(dag.parents("b")) == {"a", "c"}
    assert set(dag.parents("c")) == {"a"}

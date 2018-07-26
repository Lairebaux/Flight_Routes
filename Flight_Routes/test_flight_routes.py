import pytest
from flight_routes import FlightNetwork
from cities import cities

@pytest.fixture(scope="module")
def f():
    return FlightNetwork(cities)

@pytest.mark.parametrize("origin, destination, shortest_route",[
    ("Toronto", "Montreal", "Toronto - Montreal"),
    ("Boston", "Vancouver", "There is no flight from Boston to Vancouver."),
    ("Phoenix", "Ottawa", "There is no flight from Phoenix to Ottawa."),
    ("Toronto", "New York", "Toronto - Montreal - New York"),
    ("Los Angeles", "Chicago", "Los Angeles - Boston - New York - Chicago")
    ])
def test_shortest_routes(f, origin, destination, shortest_route):
    """
    :param str
    :return: str
    """
    assert f.find_shortest_route(origin, destination) == shortest_route


@pytest.mark.parametrize("origin, destination, all_routes",[
    ("Chicago", "New York", [["Chicago", "Denver", "New York"]]),
    ("Phoenix", "New York", "There is no flight from Phoenix to New York."),
    ("Montreal", "Vancouver", [["Montreal", "Toronto", "Vancouver"]]),
    ("Boston", "Toronto", "There is no flight from Boston to Toronto."),
    ("Los Angeles", "Chicago", [["Los Angeles", "Boston", "Providence", "New York", "Chicago"],
                                ["Los Angeles", "Boston", "New York", "Chicago"]])
    ])
def test_find_all_routes(f, origin, destination, all_routes):
    """
    :param str
    :return: str or list
    """
    assert f.find_all_routes(origin, destination) == all_routes


def test_connections(f):
    """
    :param: str
    :return: list
    """
    assert f.connections() == [("Montreal", "New York"), ("Montreal", "Toronto"),
                               ("Boston", "Providence"), ("Boston", "New York"),
                               ("Providence", "New York"), ("New York", "Chicago"),
                               ("Chicago", "Denver"), ("Chicago", "Phoenix"),
                               ("Denver", "New York"), ("Los Angeles", "Boston"),
                               ("Ottawa", "Montreal"), ("Toronto", "Ottawa"),
                               ("Toronto", "Montreal"), ("Toronto", "Vancouver"),
                               ("Vancouver", "Los Angeles")]

def test_unconnected_airports(f):
    """
    :param f:
    :return: list()
    """
    assert f.unconnected_airports() == ["Phoenix"]
    
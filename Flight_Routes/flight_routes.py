from cities import cities


class FlightNetwork:
    def __init__(self, airports=None):
        if not airports:
            airports = {}
        self.airports = airports

    def vertices(self):
        return list(self.airports.keys())

    def connections(self):
        return self._generate_connections()

    def _generate_connections(self):
        edges = []
        for node in self.airports:
            for neighbor in self.airports[node]:
                edges.append((node, neighbor))
        return edges

    def unconnected_airports(self):
        isolated = []
        for node in self.airports:
            if not self.airports[node]:
                isolated.append(node)
        if isolated == []:
            return "All nodes are connected!"
        return isolated

    def all_routes(self, departure, arrival, route=[]):
        network = self.airports
        route = route + [departure]
        if departure == arrival:
            return [route]
        if departure not in network:
            return []
        routes = []
        for city in network[departure]:
            if city not in route:
                extended_routes = self.all_routes(city, arrival, route)
                for c in extended_routes:
                    routes.append(c)
        return routes

    def shortest_route(self, departure, arrival, route, shortest_route):
        network = self.airports
        route = route + [departure]
        if departure == arrival:
            return route
        for city in network[departure]:
            if city not in route:
                if shortest_route == None or len(route) < len(shortest_route):
                    new_route = self.shortest_route(city, arrival, route, shortest_route)
                    if new_route:
                        shortest_route = new_route
        return shortest_route

    def _print_shortest(self, route):
        result = ""
        for position, city in enumerate(route):
            result += f"{city}"
            if position != len(route) - 1:
                result += ' - '
        return result

    def find_shortest_route(self, departure, arrival):
        flight = self.shortest_route(departure, arrival, [], None)
        if flight:
            return self._print_shortest(flight)
        else:
            return f"There is no flight from {departure} to {arrival}."

    def find_all_routes(self, departure, arrival):
        flight = self.all_routes(departure, arrival)
        return flight if flight else f"There is no flight from {departure} to {arrival}."


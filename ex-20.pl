% planet(Name, OrderFromSun, Type, DiameterKm, Moons)
% Type can be terrestrial or gas_giant

planet(mercury, 1, terrestrial, 4879, 0).
planet(venus, 2, terrestrial, 12104, 0).
planet(earth, 3, terrestrial, 12742, 1).
planet(mars, 4, terrestrial, 6779, 2).
planet(jupiter, 5, gas_giant, 139820, 79).
planet(saturn, 6, gas_giant, 116460, 82).
planet(uranus, 7, gas_giant, 50724, 27).
planet(neptune, 8, gas_giant, 49244, 14).

% Optional: define some moons separately
moon(earth, moon).
moon(mars, phobos).
moon(mars, deimos).
moon(jupiter, io).
moon(jupiter, europa).
moon(jupiter, ganymede).
moon(jupiter, callisto).
% Find planet type
planet_type(Name, Type) :-
    planet(Name, _, Type, _, _).

% Find number of moons
planet_moons(Name, Moons) :-
    planet(Name, _, _, _, Moons).

% Find planets with more than N moons
planets_more_than_n_moons(N, Name) :-
    planet(Name, _, _, _, Moons),
    Moons > N.

% Find planets smaller than given diameter
planets_smaller_than(Diameter, Name) :-
    planet(Name, _, _, D, _),
    D < Diameter.

% Find the order of a planet from the sun
planet_order(Name, Order) :-
    planet(Name, Order, _, _, _).

% Find planets by type
planets_by_type(Type, Name) :-
    planet(Name, _, Type, _, _).

% List all moons of a planet
moons_of_planet(Planet, Moon) :-
    moon(Planet, Moon).

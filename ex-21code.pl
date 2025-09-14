%-------------------------
% Towers of Hanoi in Prolog
%-------------------------

% hanoi(N, From, To, Aux)
% N = number of disks
% From = source peg
% To = target peg
% Aux = auxiliary peg

hanoi(1, From, To, _) :-
    write('Move disk from '), write(From), write(' to '), write(To), nl.

hanoi(N, From, To, Aux) :-
    N > 1,
    M is N - 1,
    hanoi(M, From, Aux, To),
    hanoi(1, From, To, _),
    hanoi(M, Aux, To, From).

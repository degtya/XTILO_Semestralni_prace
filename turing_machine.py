class State: 
    def __init__(self, name, is_end=False):
        self.name = name
        self.is_end = is_end

class Tape:
    def __init__(self, symbols):
        self.symbols = list(symbols)
        # První neprázdný symbol
        self.head = 0 
        while self.head < len(self.symbols) and self.symbols[self.head] == '#':
            self.head += 1

    def read_symbol(self):
        return self.symbols[self.head] if self.head < len(self.symbols) else '#'

    def write_symbol(self, symbol):
        if self.head < len(self.symbols):
            self.symbols[self.head] = symbol
        else:
            self.symbols.append(symbol)

    def move_head(self, direction):
        if direction == 'R':
            self.head += 1
        elif direction == 'L':
            self.head -= 1 if self.head > 0 else 0
        elif direction == 'S':
            pass  

class TuringMachine:
    def __init__(self, tape, states, rules, start_state):
        self.tape = tape
        self.states = {state.name: state for state in states}
        self.rules = rules
        self.current_state = self.states[start_state]
        self.step_count = 0  

    def step(self):
        self.step_count += 1  
        current_symbol = self.tape.read_symbol()
        rule_key = (self.current_state.name, current_symbol)

        if rule_key in self.rules:
            write_symbol, move_direction, next_state = self.rules[rule_key]
            self.tape.write_symbol(write_symbol)
            self.tape.move_head(move_direction)
            self.current_state = self.states[next_state]
            
            self.print_tape_state()  

            if self.states[next_state].is_end:
                print("Dosáhnuto koncového stavu:", next_state)
                return False
        else:
            print("Pro tento stav a symbol neexistuje pravidlo:", self.current_state.name, current_symbol)
            return False

        return True

    def run(self):
        self.print_initial_tape_state()
        while self.step():
            pass  
        print("Výsledek:", ''.join(self.tape.symbols))
        self.print_machine_code()
    
    def print_initial_tape_state(self):
        tape_str = ''.join(self.tape.symbols)
        print(f"Počáteční stav pásky:{tape_str}")
        print()

    def print_tape_state(self):
        tape_str = ''.join(self.tape.symbols)
        print(f"Krok {self.step_count}: {tape_str}")

    def print_machine_code(self):
        print()
        print("Pravidla:")
        for key, value in self.rules.items():
            current_state, read_symbol = key
            next_state, write_symbol, move_direction = value
            print(f"({current_state}, {read_symbol}) => ({next_state}, {write_symbol}, {move_direction})")


states = [
    State("q0"), State("q1"), State("q2"), State("q3"), State("q4"), State("q5"),
    State("q6"), State("q7"), State("q8"), State("q9"), State("q10"), State("q11"),
    State("q12"), State("q_end", is_end=True)
]

rules = {
    ('q0', '0'): ('0', 'R', 'q0'),
    ('q0', '1'): ('1', 'R', 'q0'),
    ('q0', '#'): ('x', 'R', 'q1'),

    ('q1', '0'): ('0', 'R', 'q1'),
    ('q1', '1'): ('1', 'R', 'q1'),
    ('q1', '#'): ('x', 'L', 'q2'),

    ('q2', '0'): ('n', 'L', 'q3'),
    ('q2', '1'): ('n', 'L', 'q6'),
    ('q2', 'x'): ('x', 'R', 'q12'),

    ('q3', '0'): ('0', 'L', 'q3'),
    ('q3', '1'): ('1', 'L', 'q3'),
    ('q3', 'x'): ('x', 'L', 'q4'),

    ('q4', '0'): ('a', 'R', 'q5'),
    ('q4', '1'): ('b', 'R', 'q5'),
    ('q4', 'a'): ('a', 'L', 'q4'), 
    ('q4', 'b'): ('b', 'L', 'q4'),
    ('q4', 'd'): ('d', 'L', 'q4'),

    ('q5', '0'): ('0', 'R', 'q5'),
    ('q5', '1'): ('1', 'R', 'q5'),
    ('q5', 'x'): ('x', 'R', 'q5'),
    ('q5', 'n'): ('n', 'L', 'q9'),
    ('q5', 'a'): ('a', 'R', 'q5'),
    ('q5', 'b'): ('b', 'R', 'q5'), 
    ('q5', 'd'): ('d', 'R', 'q5'),
    ('q5', '#'): ('#', 'R', 'q5'),

    ('q6', '0'): ('0', 'L', 'q6'),
    ('q6', '1'): ('1', 'L', 'q6'),
    ('q6', 'x'): ('x', 'L', 'q7'),

    ('q7', '0'): ('b', 'R', 'q5'),
    ('q7', '1'): ('a', 'L', 'q8'),
    ('q7', 'a'): ('a', 'L', 'q7'),
    ('q7', 'b'): ('b', 'L', 'q7'),
    ('q7', 'd'): ('d', 'L', 'q7'),
    ('q7', '#'): ('1', 'L', 'q5'),

    ('q8', '0'): ('1', 'S', 'q5'),
    ('q8', '1'): ('0', 'L', 'q8'),
    ('q8', '#'): ('1', 'S', 'q5'),

    ('q9', '0'): ('n', 'L', 'q3'),
    ('q9', '1'): ('n', 'L', 'q6'),
    ('q9', 'x'): ('d', 'L', 'q10'),

    ('q10', '0'): ('0', 'L', 'q10'),
    ('q10', '1'): ('1', 'L', 'q10'),
    ('q10', 'a'): ('0', 'L', 'q10'),
    ('q10', 'b'): ('1', 'L', 'q10'), 
    ('q10', 'd'): ('d', 'L', 'q10'),
    ('q10', '#'): ('#', 'R', 'q11'),

    ('q11', '0'): ('0', 'R', 'q11'),
    ('q11', '1'): ('1', 'R', 'q11'),
    ('q11', 'x'): ('x', 'R', 'q1'),
    ('q11', 'n'): ('d', 'R', 'q11'), 
    ('q11', 'd'): ('d', 'R', 'q11'),

    ('q12', '0'): ('0', 'S', 'q_end'),
    ('q12', '1'): ('1', 'S', 'q_end'),
    ('q12', 'x'): ('#', 'L', 'q12'),
    ('q12', 'd'): ('#', 'L', 'q12')
}

# Initializace
tape_input = "#####100#10#1#####"  
tape = Tape(list(tape_input))
turing_machine = TuringMachine(tape, states, rules, "q0")


turing_machine.run()
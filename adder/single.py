'''
Author: Filipe Chagas (filipe.ferraz0@gmail.com)
Description: Quantum full-adder circuit
Reference: https://www.quantum-inspire.com/kbase/full-adder/
'''

import qiskit
from qiskit import BasicAer
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from matplotlib import pyplot

'''
@brief qubit+qubit full adder
@param circ Quantum circuit object
@param a Qubit a index
@param b Qubit b index
@param cin Carry-in qubit index
@param t Target qubit index
@param cout Carry-out qubit index
'''
def make_single_adder(circ: qiskit.QuantumCircuit, a: int, b: int, cin: int, t: int, cout: int):
    circ.toffoli(a,b,t)
    circ.cx(a,b)
    circ.toffoli(b,cin,t)
    circ.cx(b,cin)
    circ.cx(a,b)
    circ.cx(cin,cout)
    circ.cx(b,cin)

'''
@brief Plot circuit drawning without inputs
'''
def draw_circuit():
    circ = qiskit.QuantumCircuit(5,1)
    print('q0: a\nq1: b\nq2: carry-in\nq3: target\nq4: carry-out')
    make_single_adder(circ,0,1,2,3,4)
    circ.draw(output='mpl')
    pyplot.show()

def test():
    backend = BasicAer.get_backend('qasm_simulator')
    (a,b,cin,t,cout) = (0,1,2,3,4)

    print('TESTING... \na + b = sum ...carry')

    for va in [0,1]:
        for vb in [0,1]:
            circ = qiskit.QuantumCircuit(5,2)
            
            #Building inputs
            if va == 1:
                circ.x(a)
            if vb == 1:
                circ.x(b)

            #Building adder
            make_single_adder(circ,a,b,cin,t,cout)
            
            #Building measurement
            circ.measure([t,cout], [0,1])

            #Testing
            job = qiskit.execute(circ, backend, shots=1)
            counts = job.result().get_counts()
            result = list(list(counts.keys())[0]) #result = [t_result, cout_result]
            t_result = result[0]
            cout_result = result[1]
            print(f'{va} + {vb} = {t_result} ...{cout_result}')


if __name__ == '__main__':
    draw_circuit()
    test()

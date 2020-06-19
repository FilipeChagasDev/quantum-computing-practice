import qiskit
from qiskit import BasicAer
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from matplotlib import pyplot
backend = BasicAer.get_backend('qasm_simulator')

# --- bell state generator circuit ---
'''
      ┌───┐     ┌─┐   
q0_0: ┤ H ├──■──┤M├───
      └───┘┌─┴─┐└╥┘┌─┐
q0_1: ─────┤ X ├─╫─┤M├
           └───┘ ║ └╥┘
c0_0: ═══════════╩══╬═
                    ║ 
c0_1: ══════════════╩═
'''

#quantum register
qregister = qiskit.QuantumRegister(2)
cregister = qiskit.ClassicalRegister(2)

#classical measurement register
circuit = qiskit.QuantumCircuit(qregister, cregister)

#gates
circuit.h(0)
circuit.cx(0,1)

#measurement
circuit.measure([0], [0]) #q[0] to c[0]
circuit.measure([1], [1]) #q[1] to c[1]
#or simply...
#circuit.measure([0,1], [0,1]) 

# ------------------------------------

 

print(circuit)
print('plotting the circuit drawning')
circuit.draw(output='mpl')
pyplot.show()

job = qiskit.execute(circuit, backend, shots=1024) #call simulator

job_monitor(job) #show job's progress

counts = job.result().get_counts() #get measurement results
print(counts) #print measurement results

#plot results
plot_histogram(counts) 
pyplot.show()

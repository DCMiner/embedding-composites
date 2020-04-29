========= ==========
Embedding Composites
========= ==========

This exercise contains four small programs which illustrate the use of 
embedding, and embedding composites, in Ocean and on the D-Wave QPU.

Exercise 1 
----------

Run the command

.. code-block:: bash

  python manual_embed_qubo.py 4

Read through the code and take a look at the
structure of the program. Notice the basic parts:

- Obtain the chainstrength from the command-line
- Obtain a sampler/solver
- Define the Q matrix
- Convert the Q matrix to a ``BinaryQuadraticModel``
- Run the problem, using ``DWaveSampler``
- Print the results

In this exercise, we have explicitly programmed the embedding of qubits 1 
and 5 into a chain. If you run the program with chainstrength 4 (the first
command-line parameter), you should see that the first six solutions have 
energy 1. They have energy 1 because one of the constraints is violated;
the two friend relationships and one enemy relationship are not simultaneously
solvable.

If you run the program with chainstrength 0.4, you will see a different
solution with lowest energy, and that solution has different values in
qubits 1 and 5, which shows that the chain between them is broken.

If you increase the chainstrength from 0.4, up to the value of 2, the
solution with the broken chain will eventually disappear, indicating that
the chainstrength has become sufficient to balance the strength of the terms 
in the QUBO.

Exercise 2 
----------

Run the command

.. code-block:: bash

  python qpu_embed.py

Read through the code and take a look at the
structure of the program. Notice the basic parts:

- Define the Q matrix
- Run the problem, using ``EmbeddingComposite(DWaveSampler)``
- Print the results

In this exercise, we submit the triangle problem directly as a QUBO
matrix, and we know that on the Chimera architecture, ``EmbeddingComposite``
will embed the triangle onto four physical qubits.
For chainstrength 5 (which is hard-coded in the program), the first six 
solutions should have the same energy, zero. One constraint is broken, and
we haven't used an energy offset, so the energy is zero.

This program does not print the embedding used by ``EmbeddingComposite``.
It is possible to return the embedding but we don't do it here.

Exercise 3
----------

Run the command

.. code-block:: bash

  python lazy_fixed_embedding_composite.py

Read through the code and take a look at the
structure of the program. Notice the basic parts:

- Define the Q matrix
- Run the problem, using ``LazyEmbeddingComposite(DWaveSampler)``
- Print the results

In this exercise, we submit the triangle problem directly as a QUBO
matrix, and we know that on the Chimera architecture, 
``LazyFixedEmbeddingComposite`` will embed the triangle onto four physical 
qubits. For chainstrength 4, the first six solutions should have the same 
energy, zero, as in the previous exercise.

This program prints the embedding before it prints the six solutions.
The embedding may look something like this:

``{0: [1645], 1: [1646, 1640], 2: [1642]}``

Variables 0 and 1 are represented by a single physical qubit, and variable 2
is represented by a chain of 2 qubits.

Exercise 4
----------

Run the command

.. code-block:: bash

  python miner_qpu.py

Read through the code and take a look at the
structure of the program. Notice the basic parts:

- Define the Q matrix
- Run the problem, using ``FixedEmbeddingComposite(DWaveSampler)``
- Print the results

Like the previous exercises, we submit the triangle problem directly as a 
QUBO matrix. In this program, though, we use Ocean's ``minorminer`` to 
explicitly find the embedding, and then we input the embedding into
``FixedEmbeddingComposite``. For chainstrength 2 (hard-coded), the first six 
solutions should have the same energy, zero, as in the previous exercise.

This program prints the embedding before it prints the six solutions.
It should like similar to the embedding found in the previous exercise.

Note also that two additional columns have been added, ``num_occurrences`` and
``chain_break_fraction``. The values of ``num_occurrences`` should be close to 
1000/6 for the first six solutions, because those solutions are equal in
energy and there is no reason to prefer one over another. There should be
no chain breaks in those first six solutions. There may be additional
solutions, of higher energy, which may include chain breaks.

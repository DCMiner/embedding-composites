# Embedding Composites

This exercise contains seven small programs which illustrate the use of 
embedding, and embedding composites, in Ocean and on the D-Wave QPUs.

## Exercise 1 

To run the demo, at the command line, type:


```bash
python manual_embed_qubo_chimera.py 4
```

If you're running in the Leap IDE, open a Terminal, and then run this command.

Read through the code and take a look at the
structure of the program. Notice the basic parts:

- Obtain the ``chainstrength`` from the command-line
- Obtain a Chimera sampler/solver
- Define the Q matrix
- Convert the Q matrix to a ``BinaryQuadraticModel``, so that we can add
  the energy offset ``-2-chainstrength``
- Run the problem, using ``DWaveSampler``
- Print the results

In this exercise, we have explicitly programmed the embedding of qubits 1 
and 5 into a chain. If you run the program with ``chainstrength`` 4 (the first
command-line parameter), you should see that the first six solutions have 
energy -6. 

Why do these six solutions have energy ``-6``?
When we formulated the equations, we designed them to have a lowest energy
of ``-3`` if all three equations are satisfied. When we added in the chain, 
though, we added in an additional constant of ``-chainstrength``.
For ``chainstrength`` of 4, the lowest possible energy is then ``-7``.
However, the solutions have energy -2 because one of the constraints is 
violated; the two friend relationships and one enemy relationship are not 
simultaneously solvable. That constraint has a penalty of 1, and so the
energies should be ``-6``.

If you run the program with ``chainstrength`` 0.4, you will see a different
solution with lowest energy, and that solution has different values in
qubits 1 and 5, which shows that the chain between them is broken.

If you increase the ``chainstrength`` from 0.4, up to the value of 2, the
solution with the broken chain will eventually disappear, indicating that
the ``chainstrength`` has become sufficient to balance the strength of the 
terms in the QUBO.

Qubits 0, 1, 4 and 5 are found in the first unit cell in a Chimera QPU.

## Exercise 2a

To run the demo, at the command line, type:


```bash
python qpu_embed_chimera.py 4
```

If you're running in the Leap IDE, open a Terminal, and then run this command.

Read through the code and take a look at the
structure of the program. Notice the basic parts:

- Obtain the ``chainstrength`` from the command-line
- Define the Q matrix
- Convert the Q matrix to a ``BinaryQuadraticModel``, so that we can add
  the energy offset ``-2``
- Obtain a Chimera sampler/solver
- Run the problem, using ``EmbeddingComposite(DWaveSampler)``
- Print the results

In this exercise, we submit the triangle problem directly as a QUBO
matrix, and we know that on the Chimera architecture, ``EmbeddingComposite``
will embed the triangle onto four physical qubits.
For ``chainstrength`` 4, the first six 
solutions should have the same energy, -2. One constraint is broken, and
if all the relationships held, the energy would be -3, so the energy is -2.

## Exercise 2b

To run the demo, at the command line, type:


```bash
python qpu_embed_pegasus.py 4
```

If you're running in the Leap IDE, open a Terminal, and then run this command.

Read through the code and take a look at the
structure of the program. Notice the basic parts:

- Obtain the ``chainstrength`` from the command-line
- Define the Q matrix
- Convert the Q matrix to a ``BinaryQuadraticModel``, so that we can add
  the energy offset ``-2``
- Obtain a Pegasus sampler/solver
- Run the problem, using ``EmbeddingComposite(DWaveSampler)``
- Print the results

In this exercise, we submit the triangle problem directly as a QUBO
matrix, and we know that on the Pegasus architecture, ``EmbeddingComposite``
will embed the triangle onto three physical qubits, so there will be no
chains.
In this problem, the ``chainstrength`` 4 shouldn't matter at all; try
different positive values. There should be the same solutions as in the
previous problem; energy -2. One constraint is broken, and
if all the relationships held, the energy would be -3, so the energy is -2.

## Exercise 3a

To run the demo, at the command line, type:


```bash
python lazy_fixed_embedding_composite_chimera.py 4
```

If you're running in the Leap IDE, open a Terminal, and then run this command.

Read through the code and take a look at the
structure of the program. Notice the basic parts:

- Obtain the ``chainstrength`` from the command-line
- Define the Q matrix
- Convert the Q matrix to a ``BinaryQuadraticModel``, so that we can add
  the energy offset ``-2``
- Obtain a Pegasus sampler/solver
- Run the problem, using ``LazyEmbeddingComposite(DWaveSampler)``
- Print the results

In this exercise, we submit the triangle problem directly as a QUBO
matrix, and we know that on the Chimera architecture, 
``LazyFixedEmbeddingComposite`` will embed the triangle onto four physical 
qubits. For ``chainstrength`` 4, the first six solutions should have the same 
energy, -2, as in the previous exercise.

This program prints the embedding before it prints the six solutions.
The embedding may look something like this:

``{0: [1645], 1: [1646, 1640], 2: [1642]}``

Variables 0 and 1 are represented by a single physical qubit, and variable 2
is represented by a chain of 2 qubits.

## Exercise 3b

To run the demo, at the command line, type:


```bash
python lazy_fixed_embedding_composite_pegasus.py 4
```


If you're running in the Leap IDE, open a Terminal, and then run this command.

Read through the code and take a look at the
structure of the program. Notice the basic parts:

- Obtain the ``chainstrength`` from the command-line
- Define the Q matrix
- Convert the Q matrix to a ``BinaryQuadraticModel``, so that we can add
  the energy offset ``-2``
- Obtain a Pegasus sampler/solver
- Run the problem, using ``LazyEmbeddingComposite(DWaveSampler)``
- Print the results

In this exercise, we submit the triangle problem directly as a QUBO
matrix, and we know that on the Pegasus architecture, ``EmbeddingComposite``
will embed the triangle onto three physical qubits, so there will be no
chains. There should be the same six solutions.

This program prints the embedding before it prints the six solutions.
The embedding may look something like this:

``{0: [4371], 1: [1268], 2: [4356]}``

As discussed in Exercise 2b, a single physical qubit is mapped to each logical qubit. The ``chainstrength`` shouldn't matter here since there are no chains.

## Exercise 4a

To run the demo, at the command line, type:


```bash
python miner_qpu_chimera.py 4
```


If you're running in the Leap IDE, open a Terminal, and then run this command.

Read through the code and take a look at the
structure of the program. Notice the basic parts:

- Obtain the ``chainstrength`` from the command-line
- Define the Q matrix
- Convert the Q matrix to a ``BinaryQuadraticModel``, so that we can add
  the energy offset ``-2``
- Obtain a Pegasus sampler/solver
- Compute the embedding, and print it
- Run the problem, using ``FixedEmbeddingComposite(DWaveSampler)``
- Print the results

Like the previous exercises, we submit the triangle problem directly as a 
QUBO matrix. In this program, though, we use Ocean's ``minorminer`` to 
explicitly find the embedding, and then we input the embedding into
``FixedEmbeddingComposite``. For ``chainstrength`` 4, the first 
six solutions should have the same energy, -2, as in the previous exercise.

This program prints the embedding before it prints the six solutions.
It should look similar to the embedding found in the previous exercise.

Note also that two additional columns have been added, ``num_occurrences`` and
``chain_break_fraction``. The values of ``num_occurrences`` should be close to 
1000/6 for the first six solutions, because those solutions are equal in
energy and there is no reason to prefer one over another. There should be
no chain breaks in those first six solutions. There may be additional
solutions, of higher energy, which may include chain breaks.

## Exercise 4b

To run the demo, at the command line, type:


```bash
python miner_qpu_pegasus.py
```


If you're running in the Leap IDE, open a Terminal, and then run this command.

Read through the code and take a look at the
structure of the program. Notice the basic parts:

- Obtain the ``chainstrength`` from the command-line
- Define the Q matrix
- Convert the Q matrix to a ``BinaryQuadraticModel``, so that we can add
  the energy offset ``-2``
- Obtain a Pegasus sampler/solver
- Compute the embedding, and print it
- Run the problem, using ``FixedEmbeddingComposite(DWaveSampler)``
- Print the results

Like the previous exercises, we submit the triangle problem directly as a 
QUBO matrix. 

In this program, though, we use Ocean's ``minorminer`` to 
explicitly find the embedding, and then we input the embedding into
``FixedEmbeddingComposite``. We know that on the Pegasus architecture, 
the triangle will be embedded onto three physical qubits, so there will be no
chains. For any ``chainstrength``, the six solutions should have the same 
energy, -2, as in the previous exercise.

Note also that two additional columns have been added, ``num_occurrences`` and
``chain_break_fraction``. The values of ``num_occurrences`` should be close to 
1000/6 for the first six solutions, because those solutions are equal in
energy and there is no reason to prefer one over another. There should be
no chain breaks in those first six solutions.

## Exercise 5

The program ``embedding_assignment.py`` is an exercise for students.
It is a Friends & Enemies problem with 5 individuals.
In our training course, we discuss this problem and how to create a QUBO to 
solve it.

Students are given the graph, and must create the QUBO dictionary (Q) that is 
provided to the D-Wave QPU and choose appropriate values for ``chainstrength``
and ``numruns``.

To run your program at the command line, type
```bash
python embedding_assignment.py
```

If you're running in the Leap IDE, open a Terminal, and then run this command.

You have 
successfully completed the exercise when you are able to see output showing 
two solutions to the problem:
::

    {0: 1, 1: 1, 2: 0, 3: 0, 4: 1} -2.0
    {0: 0, 1: 0, 2: 1, 3: 1, 4: 0} -2.0

The string is the ``sample``, and the second is the ``energy``. There should 
be two lowest-energy states for the problem.

## License

Released under the Apache License 2.0. See [LICENSE](LICENSE) file.

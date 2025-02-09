# CI2024_project-work s331163
Repository for the 2024/2025 project work of Computational Intelligence course.

## Contributors
This project has been developed in collaboration with [Federico Fortunati](https://github.com/fedefortu8) and [Mattia Ottoborgo](https://github.com/mattiaottoborgo).

## Introduction

The goal of the project was the development of a symbolic regression algorithm to extract a mathematical formula that best represents the distribution of 8 datasets.

## Methodology

In order to accomplish this task, we have implemented a genetic programming algorithm which returns a formula as a combination of different operators, input variables and constants.
The formula is obtained evolving a set of initial candidates, randomly generated, through a series of Mutations and Crossovers. Each candidate formula is represented as a tree data structure. Each node can represent either an operator, an input variable, or a constant value. The algorithm is interrupted when a target number of generations is reached or a perfect function is found. A functions is *perferct* when it can predict values with zero-error. If a perfect formula is not found, the algorithm returns the formula associated with the lowest *mean squared error* (MSE).

## Operators

The following is the list of operators implemented:

- Addition;
- Subtraction;
- Multiplication;
- Division;
- Power;
- Square Root;
- Logarithm;
- Sine;
- Cosine;
- Arctangent;
- Hyperbolic Cosine;
- Hyperbolic Sine;
- Hyperbolic Tangent;
- Exponential;
- Absolute Value.
  
## Initialization

The algorithm is initialized through the ramped half-and-half method, which consists in generating initial candidate trees through two modalities: 
- **Full method**: where each branch has dept = `max_depth`.
  Nodes at depth d < max_depth are randomly chosen from the operetors list. Nodes at max_depth are randomly chosen from the input variables or are assigned constant values.
- **Grow method**: where each branch has dept <= `max_depth`.
  Nodes at depth d < max_depth can be assigned either an operator, a variable or a constant. Nodes at depth d = Dmax are randomly chosen from the terminal set (variables and constants).
  
Each candidate has a fixed probability of 50% of being generated either by the Full method or Grow Method.

## Mutations

Mutations are applied with a low probability. The following is the list of possible mutations:

- **Ephemeral Random Constants Mutation**: Mutation applied to constants. It substitutes the current value with a random one within a fixed range;
- **Point Mutations**: Mutation applied to operators and variables. The node is substituted respectively with a randomly chosen operator and variable;
- **Mutate all tree**: Mutation applied on the candidate level. It substitutes a candidate with a newly generated one.
- **Hoist Mutation**: This Mutation samples a random subtree from an individual, and replace its genome with the selected subtree.

## Crossover

- **Simple Crossover**: Select two parents. Choose a random subtree from each parent. Swap the two subtrees between parents, to generate two new genomes. There are no constraints about the position of the selected subtrees;
- **Similar Height Crossover**: Swap subtrees with similar height. This helps in limiting the growth of candidate size.
- **Fixed Height Crossover**: Swap subtrees of fixed height.

## Evolution strategy

The genetic programming algorithm is developed as follow:

1. **Initialize the Population**: The algorithm begins by creating an initial population of candidate solutions (functions). Each candidate is generated using `generate_candidate(MAX_DEPTH, features)`. Only valid candidates are added to the population. A candidate is valid if:
  - It produces a valid output when evaluated (`evaluate_function(candidate, data)` is not `None`).
  - It contains all required variables (features).

2. **Evolution over generations**: This step is articulated as follow:
  - Parent selection through tournament selection;
  - Offspring generation through Crossover or Mutation;
  - Merge Offspring with parents;
  - Select top candidates with lowest MSE through fitness proportional method.
  - If, for a fixed number of generations, the lowest value of MSE is not further lowered, all the population, except the top individual, is re-initiated using the half and half method (*Random Restart*). 
  
In order to stay consistent with the traditional implementation of genetic programming, we have implemented mutation with a low probability. This means that the algorithm needs a consistent amount of candidates to ensure diversity among the population, which is vital to minimize the risk of converging to local optima due to lack of genotype diversity. 

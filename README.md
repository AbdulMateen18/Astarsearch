# A\* Search Algorithm Implementation

This repository contains an implementation of the A\* search algorithm for finding the shortest path between two cities on a map (Romania map in this case, with is provided as an input). The graph representation and search algorithm are implemented in Python.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Graph Input Format](#graph-input-format)
- [Example](#example)
- [Requirements](#requirements)
- [Installation](#installation)
- [Execution](#execution)
- [License](#license)

## Introduction

This project demonstrates an implementation of the A\* search algorithm, a popular pathfinding and graph traversal algorithm. The algorithm is used to find the shortest path from a start city to a destination city based on a given map of cities and the distances between them.

## Features

- Load a graph from a text file with cities, heuristic values, and distances between cities.
- Handle city names with spaces.
- Perform A\* search to find the shortest path and its total distance.
- Provide user input for start and destination cities.
- Display the path and total distance if a path is found.

## Usage

1. Prepare a graph input file (see the format below).
2. Run the Python script.
3. Input the start and destination cities when prompted.

## Graph Input Format

The input file should contain information about the cities, their heuristic values, and distances to neighboring cities. Each line represents a city and its neighbors. The format is as follows:

```
CityName HeuristicValue Neighbor1 Distance1 Neighbor2 Distance2 ...
```

### Example:

```
Arad 366 Zerind 75 Sibiu 140 Timisoara 118
Zerind 374 Arad 75 Oradea 71
Sibiu 253 Arad 140 Oradea 151 Fagaras 99 Rimnicu Vilcea 80
```

## Example

Suppose the input file `romaniamap.txt` contains the following:

```
Arad 366 Zerind 75 Sibiu 140 Timisoara 118
Zerind 374 Arad 75 Oradea 71
Sibiu 253 Arad 140 Oradea 151 Fagaras 99 Rimnicu Vilcea 80
...
```

Run the script and input the start and destination cities:

```
Please enter name of the starting city: Arad
Please enter name of the destination city: Bucharest
```

Output:

```
Path: Arad -> Sibiu -> Fagaras -> Bucharest
Total distance: 450 km
```

## Requirements

- Python 3.x

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/astar-search.git
cd astar-search
```

Ensure you have Python 3 installed on your system.

## Execution

Run the script using the following command:

```bash
python 211370194_AbdulMateen.py
```

Follow the on-screen prompts to input the start and destination cities.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

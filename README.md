# Analysis of Plane Trusses with Python - Stiffnes Matrix Method


## Table of contents

- [Overview](#Overview)
  - [Analytical data input](#Data-input)
  - [Supports data](#Supports)
  - [Joint loads](#Loading)
  - [Results of analysis](#Results)
- [Program Specifications](#Program-Specifications)
  - [Built with](#built-with)
  - [Formulas used](#Formulas)
- [Author](#author)
- [Acknowledgments](#acknowledgments)



## __Overview__

This program was developed such that it can be used to analyze any statically determinate or indeterminate plane truss, of any arbitrary configuration, subjected to any system of joint loads.

The program reads and stores the structural and loading data necessary for the analysis. The program does the following functions:

- assignment of the degree-of-freedom and restrained coordinate numbers for plane trusses
- generation of the structure stiffness matrix __S__ by assembling the elements of the member stiffness matrices
- formation of the joint load vector __P__
- evaluation of the member axial forces __Q__ and __F__
### _Data-input_
The program reads the structural and loading data necessary for analysis from the user, and stores it in the computer’s memory so that it can be processed conveniently by the program for structural analysis.

The input data necessary for the analysis of plane trusses can be divided into the following six categories:
- joint data
- support data
- material property data
- cross-sectional property data
- member data
- load data
### _Supports_
The support data consists of the number of joints that are attached to supports, the joint number, and the directions of restraints, for each support joint.

The supports are classified as follows:
- free joint
- horizontaly restrained joint
- verticarly restrained joint
- fixed/hinged joint

In the program they are contained in a list shown below:

```python
supcondition = ['P = pinned',
                'H = Horizonally restrained',
                'V = Vertically restrained ']
```

### _Loading_
The load data involves the number of joints that are subjected to external loads, the joint number, and the magnitudes of the force components in the global X and Y directions, for each loaded joint. The right hand rule is applied for sign convention.
### _Results_
After the structural and loading data necessary for the analysis has been entered, the program computes all the data using the Structure stiffness method and outputs the following results
- Structure Stiffness Matrix __S__.
- Joint displacement Vector __d__.
- Member end force vector in local coordinate system __Q__.
- Member end force vector in global coordinate system __F__.
## Program-Specifications
### _Built with_
The program was developed with [python 3](https://www.python.org/download/releases/3.0/).

The following python libraries were used.
- [Numpy](https://numpy.org/) 
- [Math](https://docs.python.org/3/library/math.html)

### _Formulas_
The joint displacements, __d__, of a structure due to an external loading, __P__, are determined by solving a system of simultaneous equations, expressed in the form __P=Sd__.

 The Structure Stiffness Matrix __S__, is formed by assembling the stiffness matrices for its individual members __K__ in the global coordinate system where __K__ is given by:

![](./formulas/global%20member%20stiffness%20matrix.png)
In the program it is expressed as:
```python
for i in range(total<e):
    cc = float(cosofel[i])**2
    ss = float(sinofel[i])**2
    cs = float(cosofel[i])*float(sinofel[i])
    
    mat = elcon[i]*numpy.array([[cc, cs, -cc, -cs],
                               [cs, ss, -cs, -ss],
                               [-cc, -cs, cc, cs],
                               [-cs, -ss, cs, ss]])

    elstmat.append(mat)
```

After the joint displacements have been established, member end displacements in the global coordinate system __v__ can be derived from __d__ by use of code numbers and used to compute the Member End forces in the global coordinate system __F__ by using __F=Kv__.

Member end forces in the local coordinate system __Q__ can be found by using the relationship __Q=TF__ where __T__ is the transformation matrix given by:

![](./formulas/transformation%20matrix.png)


## Author
This program was developed by Emmanuel Mushambi, a Civil Engineering student based in Zimbabwe who is also a programmer and a part-time Web Developer.

- Github - [Emmanuel Mushambi](https://www.github.com/Munashe-zw)
- E-mail - [Emmanuel Mushambi](mushambie7@gmail.com)
## Acknowledgments
Special thanks to Eng Marindiko, colleagues, friends and [Vishnuprasad R](https://www.youtube.com/channel/UCgROEV5T_FtY-A-MuiT8u8g/about) for their support throughout he development of this program.


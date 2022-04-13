# Analysis of Plane trusses -Stiffnes Matrix Method


## Table of contents

- [Overview](#Overview)
  - [Analytical data input](#Data-input)
  - [Supports data](#Supports)
  - [Joint loads](#Loading)
  - [Results of analysis](#Results)
- [Program Specifications](#Program-specifications)
  - [Built with](#built-with)
  - [Libraries used](#Libraries)
  - [Formulas used](#Formulas)
- [Author](#author)
- [Acknowledgments](#acknowledgments)



## __Overview__

The  objective was to develop a general computer program that can be used to analyze any statically determinate or indeterminate plane truss, of any arbitrary configuration, subjected to any system of joint loads.

The input module reads, and stores the structural and loading data necessary for the analysis. In the background the program does the following:

- assignment of the degree-of-freedom and restrained coordinate numbers for plane trusses
- generation of the structure stiffness matrix __S__ by assembling the elements of the member stiffness matrices
- formation of the joint load vector __P__
- evaluation of the member axial forces __Q__ and __F__

### _Data-input_
The input of a structural analysis program reads the structural and loading data necessary for analysis from the user, and stores it in the computer’s memory so that it can be processed conveniently by the program for structural analysis.

The input data necessary for the analysis of plane trusses can be divided
into the following six categories:
- joint data
- support data
- material property data
- cross-sectional property data
- member data
- load data

### _Supports_

The support data consists of the number of joints that are attached to supports, the joint number, and the directions of restraints, for each
support joint.

The supports can bedivived into the following types:
- free joint
- horizontaly restrained joint
- verticarly restrained joint
- fixed/hinged joint

In the program the are displayed as:

'''python
'''
![](./solution/Desktop%20Preview.jpeg)

_Mobile Preview_

![](./solution/Mobile-preview.jpeg)

### Loading

- Solution files: [GitHub Repository](https://github.com/Munashe-zw/Testimonials-grid-section-challenge-on-Frontend-Mentor.git)
- Solution URL: [Add solution URL here](https://munashe-zw.github.io/Testimonials-grid-section-challenge-on-Frontend-Mentor/)

### Results

## Program Specifications

### Built with

- CSS custom properties
- Flexbox
- CSS Grid


### Libraries used

l learnt using CSS Grid layout system, from grid elements, display properties, grid columns, grid rows, grid gaps and implemened them in this project. And also learnt using markdown to document this project.

During the project l could have easily implemented the mobile view with the snippet below:


```css
@media(max-width: 678px){
    .container{
      display: block;
    }

    .card{
        margin: 20px auto;
    }
}
```
But for the sake of learning CSS Grid l used the method below:

```css
@media(max-width: 678px){
    .container{
        grid-template-columns: 1fr;
        width: 100%;
    }

    /* Grid Sections */
    .card:nth-of-type(1){
        grid-column: 1;
    }

    .card:nth-of-type(4){
        grid-column: 1; 
        grid-row: 4;
    }

    .card:nth-of-type(5){
        grid-column: 1; 
        grid-row: 5;
    }
}
```


## Author
This program was written by Emmanuel Mushambi a civil engineering student and a part time programmer and Web developer.

- Website - [Emmanuel Mushambi](https://www.github.com/Munashe-zw)
- Frontend Mentor - [@Munashe-zw](https://www.frontendmentor.io/profile/yourusername)


## Acknowledgments



# lisp_compiler

## Objective 

In this job, we valid [**lambda expressions**](https://www.gnu.org/software/emacs/manual/html_node/elisp/Lambda-Expressions.html) in LISP programming language. Developed with [PLY](http://www.dabeaz.com/ply/ply.html#ply_nn23)

## Capture

![alt text][capture]

## How to run

In the project folder

``` python main.py ```

## Lambda structure 

(lambda (arg-variables...)
       [documentation-string]
       body-forms...)

The first element of a lambda expression is always the symbol lambda. This indicates that the list represents a function. The reason functions are defined to start with lambda is so that other lists, intended for other uses, will not accidentally be valid as functions.

The second element is a list of symbols—the argument variable names. This is called the lambda list.

The documentation string is a Lisp string object placed within the function definition to describe the function for the Emacs help facilities.

The rest of the elements are the body of the function: the Lisp code to do the work of the function. [Structure](https://www.gnu.org/software/emacs/manual/html_node/elisp/Lambda-Components.html#Lambda-Components)

## Examples

| Example                                            | Return           |
| -------------------------------------------------- |:----------------:|
| (lambda (x) (* x 5))                               | CORRECT          |
| (lambda (x) (+ x 5 8 5))                           | CORRECT          |
| (lambda (x &optional y) (+ x y))                   | CORRECT          |
| (lambda (x &optional y z) (/ x y z))               | CORRECT          |
| (lambda (x &optional y &optional z) (/ x y z))     | INCORRECT        |
| (lambda (x &optional y &rest z) (/ x y z))         | CORRECT          |
| (lambda (x &optional y &rest z) (* (+ x 5) 5))     | CORRECT          |
| (lambda (x) (* (+ (+ x 5) 5) 5 6 6 5))             | CORRECT          |
| (lambda (x &rest y) (* (exp (+ x 5) 5)))           | CORRECT          |
| (lambda (&optional y) (if (y) (write y) (exp 2)))  | CORRECT          |


### Developers

 * Geancarlo Murillo
 * Daniel Saigua
 * Tai Yu Chen

###### LISP compiler for Programming Languages subject | ESPOL 2018

[capture]: https://github.com/gcmurillo/lisp_compiler/blob/master/capture.JPG
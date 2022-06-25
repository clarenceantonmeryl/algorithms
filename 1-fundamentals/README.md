## 1. Fundamentals
- Algorithm: A method of solving a problem, which is implemented in code.
- Programming model: the code that is used to implement an algorithm.
- Data structure: The type that a data is found in (eg. int, string)

Anatomy of a Java program:

- Class
    - static void functions -> no return values, only side effects.
      - variable declarations
      - conditional statements
      - loops
      - calling a local method
      - expressions
    - static functions -> have a return value.
        - same as static void function
        - return statement


- Primitive data types: integer, real number, boolean. Possible operations on those values and expressions that define values.
- Statements: define computations that occur involving data types and variables (eg. declarations, assignments, conditionals, loops, calls, returns).
- Arrays: multiple values of the same data type.
- Strings: sequences of characters.
- Static methods: code that can be reused and makes programs modular.
- Input/output sets: communication between program and outside world.
- Data abstraction: definition of non-primitive data-types and object-oriented programming.


### Primitive data types

Set of values and set of operations.
- Integers (int), for arithmetic operations.
- Real numbers (double), for the same purpose as int.
- Boolean (boolean), true/false values.
- Characters (char), alphanumeric characters and symbols

| term                | examples                        | definition                                                                                        |
|---------------------|---------------------------------|---------------------------------------------------------------------------------------------------|
| primitive data type | int, double, boolean, char      | a set of values and a set of operations on those values                                           |
| identifier          | a, abc, Ab$, a_b, ab123, lo, hi | a sequence of letters, digits, _, $, the first of which is not a digit                            |
| variable            | any identifier                  | names a data-type value                                                                           |
| operator            | +,-,*,/                         | names a data-type operation                                                                       |
| literal             | int, double, boolean, char      | source-code representation of a data-type value                                                   |
| expression          | int, double, boolean            | a literal, variable, or sequence of operations on literals and/or variables that produces a value |

***Expressions***: literal (or expression), operator, literal (or expression)
- operators `*`, `/` and `%` are applied before `+` and `-`
- `!` is applied before `%%`, then `||`
- `()` overrides the rules.

***Type conversion***: changing data to different data-types. (3.7 becomes 3 in int and 3 becomes 3.0 in double)

***Comparisons***: produce boolean value
- `==` equal
- `!=` not equal
- `<` less than
- `>` greater than
- `<=` less than or equal to
- `>=` greater than or equal to

***Other primitive types***:
- 64-bit int (`long`)
- 16-bit int (`short`)
- 16-bit characters (`char`)
- 8-bit int (`byte`)
- 32-bit single-precision real numbers (`float`)

Statement: define computation by creating and manipulating variables, assigning data-type values to them, and controlling the flow of execution of operations.
Organised in blocks of curly braces.

Declaration: create variables of a specific type and names them with identifiers.

Assignment: associate data-type value with variables.

Conditionals: affects flow of execution -- execute one of two blocks of code depending on the condition
> `if (<boolean expression>) {<block statements>}` \
  `else {<block statements>}`

Loops: affects flow of execution -- execute the block as long as given condition is true
> `while (<boolean expression>) {<block statements>}`
- Break: immediately exits loop
- Continue: immediately begins next iteration of loop
> `for (<initialize>; <boolean expression>; <increment>)` \
 `{` \
 `<block statements>` \
 `}`

Calls and returns: relate to static methods and also affect the flow of execution and organises code.

| statement                | examples                                                        | definition                                                           |
|--------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------|
| declaration              | `int i;` <br/> `double c;`                                      | create a variable of a specified type, named with a given identifier |
| assignment               | `a = b + 3;` <br/> `discriminant = b*b - 4.0*c;`                | assign a data-type value to a variable                               |
| initializing declaration | `int i = 1;` <br/> `double c = 3.141592625;`                    | declaration that also assigns and initial value                      |
| implicit assignment      | `i++;` <br/> `i += 1;`                                          | `i = i + 1;`                                                         |
| conditional (if)         | `if (x < 0)` <br/> `x = -x;`                                    | execute a statement depending on boolean expression                  |
| conditional (if/else)    | `if (x > y)` <br/> `max = x;` <br/> `else` <br/> `max = y;`     | execute one or the other statement depending on boolean expression   |
| loop (while)             | `int power = 1;` <br/> `while (power <= n)` <br/> `power *= 2;` | execute statement until boolean expression is false                  |
| loop (for)               | `for (int i = 1; 1 <= n; i++)` <br/>  `sum += 1.0/i;`           | compact version of while statement                                   |
| call                     | `int key = StdIn.readInt();`                                    | invoke other methods                                                 |
| return                   | `return false;`                                                 | return from a method                                                 |



**Arrays**
- Stores sequence of values that are all of the same type. a[i] refers to the i<sup>th</sup> value in the array.

Array initialisation
```
# long form

# declaration
double[] a;

# creation
a = new double[n];

# initialization
for (int i = 0; i < n; i++)
        a[i] = 0.0;
```

```
# short form
double[] a = new double[n]

# initializing declaration
int[] a = {1, 1, 2, 3, 5, 8};

```

2-dimensional arrays are created using an extra set of square brackets ([]). A value is accessed using a[i][j], which is an entry at row i, column j.
```
double[][] a = new double[m][n];
```

**Static and Instance Methods**

Method: a series of computation that is defined by a sequence of statements. They take arguments and compute a return value or causes a side effect.

Static method signature: `public static return type, method name, arguments, body`
```
public static double sqrt(double c) {
    if (c < 0) return Double.NaN;
    double eps = 1e-15;
    double t = c;
    while (Math.abs(t - c/t) > eps * t)
        t = (c/t + t) / 2.0;
    return t;
}
```

- Static methods do not require an instance of the class to be created before calling it. (eg. `Math.sqrt(10)`)
- Instance methods do require an instance of the class to be created before calling it. (eg. `inst = new ClassName(); inst.funcName();`)

**Recursion**
- When a method calls itself to make code more efficient
    - Recursion must have a base case -- include a conditional statement as the first statement in the program that has a return.
    - Must address a subproblem that is smaller in some sense.
    - Should not address subproblems that overlap.

**APIs**
- Application programming interfaces that list the library name and the signatures and short descriptions of each of the methods used.
- Client: a program that calls a method in another library.
- Implementation: Java code that implements the methods described in the API.

```
public class Math

static double abs(double a)                 absolute value of a
static double max(double a, double b)       maximum of a and b
static double min(double a, double b)       minimum of a and b
```

**Strings**
- A sequence of characters.
- Concatenation: Joins two or more Strings into one String.
- Conversion: `static int parseInt(String s)` converts String to int. `static String toString(int i)` converts int to String.

**Input and Output**
- Inputs are the arguments.
- Outputs are the return values.


Before you begin trying to make a Minecraft mod, it is important that you are comfortable with the Java programming language. There exist better ways to learn Java for beginners than this document but I'll make an attempt. If you've already got a good understanding of Java, I encourage you to skip this and get started making your mod. Otherwise, if you're already comfortable with another programming language, this will be trivial to learn, if not might be kinda difficult. 

## Data Types

In Java, there are two kinds of data types: primitive and** r**eference.

Primitive data types are the simple building blocks of information your programs can store. Such as, 

`byte`, can store values of `-128` to `127`  (1 byte) 
`short`, can store value of `-32768` to `32767` (2 bytes) 
`int`, can store value of `-2147483648` to `2147483647` (4 bytes) 
`long`, can store value of `-9223372036854775808` to `9223372036854775807` (8 bytes)
`char`, can store characters (2 bytes) 
`double`, can store decimal numbers (8 bytes)
`float`, can store decimal numbers (4 bytes) 
`boolean`, can either store `true` or `false` (1 bit) 

Using smaller data types such as `byte` over a seemingly better `int` or `long` is useful for saving memory. When you have simple variables and you know their value will never go larger than 127 there's no reason to use a whole `int`.

Reference data types are objects of a class or an interface. They can have much more complex behaviours (through methods) and store multiple pieces of data (both primitive and reference). Some examples are `String` (which holds an immutable sequence of characters like a word or a paragraph) and`Array` (which holds a dynamic sequence of any type) but there are many others and you can even make your own :)

> Reference data types are objects, while primitive data types aren't. Primitive data types can not point to `null` reference while reference data types can. The value of reference data types defaults to `null`, however. In the case of primitives, their default value is assigned (the minimum value). 

## Variables

A variable holds one piece of data. They have a type (any primitive or reference type) and a name (so you can refer to it in your code).

First, we will begin with the basic syntax of declarations. To declare a variable, we simply choose the type of the variable (we will use int) and give it a name.

    int foo;

To declare multiple variables with the same type, we can use:

    int foo, foo1, foo2;

> Every declaration ends with a `;` character, which essentially means "end of command", a command can be anything such as a method call or a variable declaration.

Of course, this works with other types as well:

    String foo;
    String foo2, foo3, foo4;

To give our variable a value other than the default we can either initialize it with a value:

    int foo = 1;

Alternatively, first declare the variable and later in the code give it something to store. 

    int foo;
    foo = 1;

## Operators 

Operators act between two values. The five arithmetic operators are fairly self explanatory:

+,  addition 
-,  subtraction 
/,  division 
*, multiplication 
%, modulo (remainder) 

> These can be only used while working with primitive types. The only exception is a string concatenation, when we want to put two sequence of characters together.

    int foo = 1;
    int bar = 2;
    
    int result = foo + bar;

Now result stores the value 3. Also we don't have to declare a those variables called `foo, bar`. It can also be written like this

    int result = 1 + 2;

> If you try to divide by zero the program will crash with an `ArithmeticException`. We'll talk more about exceptions later.

Of course, the other operators work the same way. 

    double speed = 1.0 / 8.0; // speed is now 0.125
    double four = speed * 32;
    
    // modulo gives the remainder of a devision
    int thing = 12 % 10; // thing is 2
    
    // delare a string by putting text in quotes
    String name = "Luke";
    String greeting = "Hi " + name;

> Note that any text on a line past `//` is ignored by the complier. This is called a comment. They can be used to describe whats going on in your code so people who read it can understand more easily. you can also make a multi-line comment by putting anything between `/*` and `*/`

There are 3 boolean operators.

`!`, not, which inverts the value
`&&`, and, which checks that both of the values are true
`||`, or, which checks that at least one of the values is true

    boolean foo = true;
    boolean bar = !foo;  // false
    boolean baz = foo && bar; // false
    boolean bam = foo || bar; // true

There are 6 types of equality operator. They are used to compare 2 numbers and evaluate to a boolean. 

`==`, compares a value when used on primitive types and a reference when used on reference types 
`>=`, is greater than or equal 
`<=`, is less than or equal 
`>`, is greater than 
`<`, is less than 
`!=`, is not equal to (inverse of ==) 

    boolean foo = 3 > 1; // true
    boolean bar = 9 == (3 + 4); // false

`instanceof` is used for checking if an ****object**** is an instance of a particular class or it's subtype. This will make more sense once we learn more about objects. Example,

    String foo = "hello world";
    boolean result = foo instanceof String; // true
    boolean other = foo instance of ArrayList; // false

Operators that evaluate to booleans can be chained together to form boolean expressions. These expressions can anywhere a boolean is needed.

    boolean foo = 1 < 2 || 2 < 1;

The variable `foo` will now hold the value `true`, even though the second expression returns `false`. That is because its an or operator and the first expression has returned `true`.

    boolean foo = 1 < 2 && 2 < 1;

## If Statements

An if statement controls the flow of your program. You can specify code to run only if a boolean expression (known as a condition in this context) is true. 

    int foo = 5;
    int bar = 10;
    
    if (bar > foo) {
       // run some code
    }

---

to be continued...

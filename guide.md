# Week 6 Discussion Guide

1. The course lecture "Introduction to Namespaces and Scope" (Module 5.1) defineds namespaces and scope in the following ways (taken from Python documentation)

Namespace: A namespaces is a mapping from names to objects. There is no relation between names in different namespaces. Two different modules may both define a function `maximize` without confusion - users of the modules must prefix it with the module name.

Scope: A scope is a textual region of a Python program where a namespace is directly accessible. "Directly accessible" here means that an unqualified reference to a name attempts to find the name in the namespace.

2. 
    1. There are three versions of the sum function. This code uses the built-in sum function on line 7. A user-defined sum function on line 9, and a sum function imported from NumPy (line 20, used on line 22). This version of the sum function will be the one that is used in `squared_sum` on line 30, as it is the most recent definition of the sum function.

    2. See answer above

    3. The variable `add` occurs twice. The scope of the first variable is 12-16. The scope of the second is 30-34.

    4. The variable `my_list` has scope of lines 18 to 26.

    5. `test_list` is in the global namespace.

    6. Consider that the following code is added. Write what the output number will be, and trace the execution of the code. Write, in order, the line numbers that will be executed to evaluate this task. **Share your line numbers** in the shared 

```python
mean( [ squared_sum([1, 4, 5]), sum(test_list) ] )
```

* `squared_sum([1, 4, 5])` will be evaluated first. This will go to line 28 - 30. At line `30`, the function will call the user-defined `sum` function on line 9.
* `sum(test_list)` will be evaluated next. This will go to line 9 and exit the function at line 16.
* `mean` will be evaluated last. This will go to line 18 and exit the funciton at line 26. The NumPy version of sum is used in this function.

## Bash Scripting an Python Data Types

Students should use `wget` or `curl` to download the file.

1. You can use a Python `set` to quickly get all unique substances. This is because a set only contains unique elements. 
2. Students might choose to loop over unique substances defined in the set and count the number of times each substance occurs in the list. The easiest way to do this is with the `count` method of a list.
3. Students can loop over the dictionary keys and check if the key ends with or contains `(s)`.

### Scripting
The script should use `wget` or `curl` to download the file. It should then use Python to perform the tasks. They can call their Python script in the bash script by putting `python script_name.py`.


### Python Collections
The `Counter` object in collections would be useful for task (2) in the Python Data types section.
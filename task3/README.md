# average_calculator.py

The `average_calculator.py` script contains a function, `avg()`, which calculates the average of a 
given set of numerical inputs. The function is designed to accept either a single iterable (excluding 
strings) or multiple comma-separated numbers. In the first case, it computes the average of all 
elements within the iterable. In the latter case, it computes the average of all the arguments.

## basic_classes.py

The `basic_classes.py` script defines a series of classes representing a basic employee-company model. 
It contains three classes: `Person`, `Employee`, and `Company`. The `Person` class serves as the base 
for human individuals with attributes for `name` and `age`. The `Employee` class, a subclass of `Person`, 
extends this with `employee_id` and `position` attributes. The `Company` class represents a business entity 
that holds a list of `Employee` instances, providing functionality to add an `Employee` to its list.

# animal.py

The `animal.py` script enhances the class hierarchy to model complex interactions and relationships in 
a pet ownership ecosystem. It extends the `Human` and `Person` classes by adding new attributes, such as 
a tax number. It introduces the `Enterprise` class, which is designed to own `Pet` instances.

In addition, this script establishes the `Vaccine` class representing different types of vaccines and 
a `Chip` class with subclasses for distinct animal ID chips, enhancing the representational detail of 
each `Pet`. Each `Pet` instance now contains an attribute for a chip and a vaccine, providing a more 
realistic and intricate model of pet ownership and identity tracking.
# What will happen if two modules in the same package have a circular import (Module A imports Module B, and Module B imports Module A)? How can you resolve it?
# What will happen if two modules in the same package have a circular import (Module A imports Module B, and Module B imports Module A)? How can you resolve it?

When Module A imports Module B and vice versa, Python creates a loading loop where neither module finishes initializing. This results in an ImportError or AttributeError because a module attempts to access names from the other before they are defined, often displaying the message: "cannot import name 'X' from partially initialized module 'Y' (most likely due to a circular import)".

Circular imports can be resolved using the following:

1.Deferred Imports: Move the import statement inside the function or method that uses the imported object. This ensures the module is fully loaded by the time the code executes, avoiding the initialization loop.
2.Extract Shared Code**: Identify common dependencies between the two modules and move them into a third, independent module (e.g., `common.py`). Both original modules then import from this new module instead of each other.
3.Merge Modules: If the modules are tightly coupled and small, combine them into a single file to eliminate the dependency cycle entirely.
4.Type Hint Guards: If the circular import is only for type checking, use `if TYPE_CHECKING:` to import classes only during static analysis, preventing runtime conflicts.
5.Dependency Injection: Pass objects as arguments to functions or constructors rather than importing them directly, breaking the direct coupling between modules.
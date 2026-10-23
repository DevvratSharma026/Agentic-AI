# Python Revision Checklist

## Study Progress

- [ ] Day 1 completed
- [ ] Day 2 completed
- [ ] Day 3 completed
- [ ] Day 4 completed
- [ ] Final mini-project completed

---

## Day 1: Data types, loops, comprehensions, and conditionals

- [ ] Review and practice `dict`, `list`, `set`, and `tuple` basics.
- [ ] Complete the Word Counter exercise.
  - Use a dictionary and Counter-style logic.
  - Count word frequency.
  - Print the top 5 using `sorted()` with a lambda.
  - Topics: DataTypes, Dictionary, Loops
- [ ] Complete the Data Cleaner exercise.
  - Strip spaces and clean strings.
  - Title-case names.
  - Drop empty values.
  - Build a dict comprehension and a set comprehension.
  - Topics: All three comprehensions, stringsDay 1: Data types, loops, comprehensions, conditionals

Word counter: take a paragraph, then use a dict, Counter-style logic, and a loop to count word frequency. Print the top 5 using sorted with a lambda. (DataTypes, Dictionary, Loops)
Data cleaner: given a list of messy strings like [" Alice ", "BOB", "", "carol"], use a list comprehension to strip, title-case, and drop the empty ones. Then build a dict comprehension (name → length) and a set comprehension of the unique first letters. (All three comprehensions, strings)
Grade classifier: loop over a dict of student marks with enumerate and zip. Use if/elif/else for grades, and use the walrus operator once to avoid computing a value twice. (Conditionals, Loops, walrus, enumerate, zip)

Day 2: Functions, generators
4. Function toolkit: write one function each with default args, *args, **kwargs, and keyword-only args. Then write a closure using nonlocal (a counter factory). (Functions, scopes)
5. Streaming reader: write a generator that yields a large text file line by line, and another generator that takes it and yields only lines containing a keyword. Chain them. (Generators, yield)
6. Token dispenser: write an infinite generator that yields IDs. Use send() to reset it and close() to stop it, then use yield from to combine two generators. (Generators advanced)

Day 3: Decorators, exceptions
7. Decorators: write a @timer decorator and a @retry(times=3) decorator that takes arguments. Use functools.wraps in both. (Decorators)
8. Auth decorator: write @require_role("admin") that raises PermissionError if a user dict lacks the role. (Auth decorator)
9. Custom exceptions: write a ValidationError class and a function that reads a JSON file and validates the fields. Handle FileNotFoundError, JSONDecodeError, and your custom error with try/except/else/finally. (Exception handling, file handling)

Day 4: OOP, then the mini-project
10. Class design: write a BankAccount class with @property for the balance, validation in the setter, a @classmethod alternate constructor, and a @staticmethod helper. (OOP)
11. Inheritance vs composition: write Animal → Dog/Cat with super(), then a Logger class used by composition in another class. Print Dog.__mro__ and explain it in a comment. (Inheritance, MRO)
12. Mini-project (the gate to move on): build a CLI that reads a JSON file of tasks and filters them with comprehensions. It should stream results with a generator, use a logging decorator, raise a custom exception on bad data, and model tasks as classes. If you finish this with little lookup, you’re done revising.
- [ ] Complete the Grade Classifier exercise.
  - Use `enumerate()` and `zip()`.
  - Apply `if/elif/else` logic.
  - Use the walrus operator once.
  - Topics: Conditionals, Loops, walrus operator, `enumerate()`, `zip()`

---

## Day 2: Functions and generators

- [ ] Review function concepts: parameters, return values, and scope.
- [ ] Complete the Function Toolkit exercise.
  - Default arguments
  - `*args`
  - `**kwargs`
  - Keyword-only arguments
  - Closure using `nonlocal`
  - Topics: Functions, scopes
- [ ] Complete the Streaming Reader exercise.
  - Write one generator to read a file line by line.
  - Write another generator to filter matching lines.
  - Chain them together.
  - Topics: Generators, `yield`
- [ ] Complete the Token Dispenser exercise.
  - Write an infinite generator.
  - Use `send()` to reset it.
  - Use `close()` to stop it.
  - Use `yield from` to combine two generators.
  - Topics: Advanced generators

---

## Day 3: Decorators and exceptions

- [ ] Review decorator syntax and function wrapping.
- [ ] Complete the Decorators exercise.
  - Write a `@timer` decorator.
  - Write a `@retry(times=3)` decorator.
  - Use `functools.wraps` in both.
  - Topics: Decorators
- [ ] Complete the Auth Decorator exercise.
  - Write `@require_role("admin")`.
  - Raise `PermissionError` when required role is missing.
  - Topics: Auth decorator
- [ ] Complete the Custom Exceptions exercise.
  - Create a `ValidationError` class.
  - Read a JSON file safely.
  - Validate fields.
  - Handle `FileNotFoundError`, `JSONDecodeError`, and custom exceptions.
  - Use `try/except/else/finally`.
  - Topics: Exception handling, file handling

---

## Day 4: OOP and mini-project

- [ ] Review OOP concepts: classes, objects, attributes, and methods.
- [ ] Complete the Class Design exercise.
  - Build a `BankAccount` class.
  - Use `@property` for balance.
  - Validate values in the setter.
  - Add a `@classmethod` alternate constructor.
  - Add a `@staticmethod` helper.
  - Topics: OOP
- [ ] Complete the Inheritance vs Composition exercise.
  - Create `Animal`, `Dog`, and `Cat` using `super()`.
  - Create a `Logger` class.
  - Use composition in another class.
  - Print `Dog.__mro__` and explain it in a comment.
  - Topics: Inheritance, MRO
- [ ] Complete the Mini-Project.
  - Read a JSON file of tasks.
  - Filter tasks using comprehensions.
  - Stream results using a generator.
  - Use a logging decorator.
  - Raise a custom exception on invalid data.
  - Model tasks as classes.

---

## Final Goal

- [ ] I can explain and apply all core Python topics covered in this revision.
- [ ] I can write clean Python programs without frequent lookup.
- [ ] I am ready to move to the next level of practice or projects.

> Tip: Mark each box as you finish it to track your progress. 
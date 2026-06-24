---
name: test-agent
description: Use this skill when creating, reviewing, or improving Python unit tests.
---

# Test Writing Skill

## Goal
<!-- Goal -->
This skill describes how to write tests for Python functions using pytest. It helps generate test cases based on function behavior.

## Scope
<!-- Scope -->
Apply such skill for unit tests

## Process
<!-- Process -->

1. Understand the function behavior
2. Identify inputs and expected outputs
3. Define test cases
4. Write pytest functions
5. Keep tests simple and independent

## Rules
<!-- Rules -->

- Use the AAA (Arrange-Act-Assert) pattern
- Prefer <pytest.mark.parametrize> instead of multiple tests
- Add docstring only for complex tests
- Do not include multiple asserts on a single test 

## Output Format
<!-- Output Format -->

Follow the next guidelines when creating files and test names

- Name each test as test_<function>
- Use <methodname><expectedbehavior><stateundertest> on test names
- Name each test file as test_<file>

## Example
<!-- Example -->

### Function to be Tested

```python
def multiply(a, b):
    return a * b
```

### Test Sample

```python
def test_multiply_positive_numbers():
    # Arrange
    a = 2
    b = 3

    # Act
    result = multiply(a, b)

    # Assert
    assert result == 6

```

## Edge Cases
<!-- Edge Cases -->

Cover edges cases when necessary

- Invalid inputs
- Extreme values
- Unexpected behavior
- Expected errors
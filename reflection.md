Reflection Questions
Added these answers 
Which issues were the easiest to fix, and which were the hardest? Why?
 Easiest: The Trailing Whitespace and Line Too Long errors were the easiest logically, as they only required pressing Delete or breaking a line with parentheses.
 Hardest: The Unsafe Global State was the most challenging because it required a major refactoring. Instead of a quick line fix, I had to modify the signature of every function (def func(item, qty) -> def func(inventory, item, qty)) and update every call in main(). This demonstrated the largest gain in code architecture.
Did the static analysis tools report any false positives? If so, describe one example.
Yes. When trying to achieve the 10/10 score, Pylint often flagged the use of standard Python f-strings in logging functions (e.g., logging.warning(f"Message...")) with the W1203 (logging-fstring-interpolation) warning.
This is a false positive in modern Python, as f-strings are idiomatic. Pylint prefers the older, specific format (logging.warning("Msg: %s", var)) for lazy evaluation. For the final code, this warning was effectively ignored because the f-string usage is clearer and superior for style.
How would you integrate static analysis tools into your actual software development workflow?
I would integrate static analysis as a mandatory quality gate at two stages:
1. Local Development (Pre-commit Hook): Use the pre-commit framework to automatically run Flake8 (for style) and Bandit (for security) on staged files before a commit is allowed. This catches simple, low-effort errors instantly, preventing bad code from entering version control.
2. Continuous Integration (CI) Pipeline: Set up GitHub Actions to run a full analysis (Pylint and Bandit) on every Pull Request (PR). The PR should be automatically blocked or marked as "Failed" if:
o Bandit finds any High- or Medium-severity issues.
o The Pylint score is below a pre-set threshold (e.g., 9.5/10).
What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
 Robustness: The code is far more stable. Fixing the mutable defaults and broad exception clauses eliminated hidden bugs and ensured that only expected errors are handled, preventing application failures from being masked.
 Code Architecture: Removing the global keyword (the hardest fix) significantly improved the code quality. Functions are now pure, accepting data as arguments, which makes the code modular, easier to test, and ready for future scaling.
 Security: Removing the eval() call and using specific exception handling hardened the application against code injection and unexpected failures.

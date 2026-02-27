# FEEDBACK

## Testing The Quiz
- First instance of clearing the terminal leaves some bash text on screen (we fixed by clearing terminal twice the first time)

## Code
- Great comments!

### `display_question()`
- Good use of block string for large interpolated string, much cleaner/more human-readable, we used several print statements (and a for loop for printing `question['options']`)

### `get_user_answer()`
- When user input is saved, we saved using `upper()` so we wouldn't have to call it multiple times when validating and returning. Nothing wrong with either approach.

### `check_answer()`
- When comparing user answer with `question['answer']`, technically no need to use `upper()` on `question['answer']` since they are already uppercase, but good preventative measure.

### `display_feedback()`
- Cool symbols added for correct (checkmark) and incorrect (x), also incorrect colored red. Looks great!
- Coloring uses built-in syntax, same as us!

### `run_quiz()`
- Uses try/except for category selection, exits program with error if non-number enterred
- After try/except, checks if entry is less than 1 **AND** greater than 7, so it is never true, should use `or`. If it was it states running all categories then exits program with error.
-  When enumerating through questions, category is checked and skipped if not matching selected category, meaning quiz states 10 questions, and skips numbers. Our approach would have been making a separate list before enumerating through, but still functional.
- Timer implemented very cleanly, but no punishment yet.